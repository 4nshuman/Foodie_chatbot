from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import json
import smtplib
from concurrent.futures import ThreadPoolExecutor
from email.message import EmailMessage

import requests
from rasa_sdk import Action
from rasa_sdk.events import SlotSet

import zomatopy

restaurant_email_list = []
meal_estimate = {}


class ActionSearchRestaurants(Action):

    def __init__(self):
        config = {'user_key': '5faeea4aac0526ad50539c0b87a5fd15'}
        self.zomato = zomatopy.initialize_app(config)

    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):

        # Get location from slot
        location = tracker.get_slot('location')

        # Get cuisine from slot
        cuisine = tracker.get_slot('cuisine')
        # Get budget criteria from slot and set minimum cost and max cost
        budget_criteria = tracker.get_slot('price')
        cost_min = 0
        cost_max = 1000
        if budget_criteria == 'low':
            cost_max = 300
        elif budget_criteria == 'mid':
            cost_min = 300
            cost_max = 700
        else:
            cost_min = 700

        results, lat, lon = self.get_additional_location_details(location)

        if results == 0:
            # Zomato API could not find details for this location.
            restaurant_exist = False
            dispatcher.utter_message(
                'I am sorry, no restaurants found in this location.\n' +
                'Check the location name or try with a different location')
        else:
            restaurant_result_dictionary = self.get_restaurants(lat, lon, cost_min, cost_max, cuisine)

            # Filter the results based on budget
            budget_dictionary = [single_restaurant for single_restaurant in restaurant_result_dictionary if
                                 ((int(single_restaurant['restaurant']['average_cost_for_two']) > cost_min) & (
                                         int(single_restaurant['restaurant']['average_cost_for_two']) < cost_max))]
            # Sort the results according to the restaurant's rating
            budget_dictionary_rating_sorted = sorted(
                budget_dictionary, key=lambda k: float(k['restaurant']['user_rating']['aggregate_rating']),
                reverse=True)

            # Build the response
            response = ''
            restaurant_exist = False
            if len(budget_dictionary_rating_sorted) == 0:
                dispatcher.utter_message('Sorry, no results found that would fit in the provided budget.' + '\n')
            else:
                # Pick top 5 to display in chat window
                budget_dictionary_rating_top5 = budget_dictionary_rating_sorted[:5]
                # Pick top 10 to email to the user, if required
                global restaurant_email_list
                restaurant_email_list = budget_dictionary_rating_sorted[:10]
                if restaurant_email_list and len(restaurant_email_list) > 0:
                    restaurant_exist = True
                for restaurant in budget_dictionary_rating_top5:
                    response = response + restaurant['restaurant']['name'] + ' in ' + \
                               restaurant['restaurant']['location']['address'] + \
                               ' has been rated ' + \
                               str(restaurant['restaurant']['user_rating']['aggregate_rating']) + '\n' + '\n'
                dispatcher.utter_message(
                    'Here are our picks !' + '\n ==================================================== \n' + response + '\n ==================================================== \n \n')
        return [SlotSet('restaurant_exist', restaurant_exist)]

    def get_additional_location_details(self, location):
        # Get location details including latitude and longitude
        location_detail = self.zomato.get_location(location, limit=1)
        d1 = json.loads(location_detail)
        lat = 0
        lon = 0
        results = len(d1['location_suggestions'])
        if results > 0:
            lat = d1['location_suggestions'][0]['latitude']
            lon = d1['location_suggestions'][0]['longitude']
        return results, lat, lon

    @staticmethod
    def get_restaurants(lat, lon, budgetmin, budgetmax, cuisine):
        cuisines_dict = {'american': 1, 'bakery': 5, 'biryani': 7, 'chinese': 25, 'italian': 55, 'cafe': 30,
                         'mexican': 73, 'north indian': 50, 'south indian': 85}
        restaurant_result_dictionary = []
        executer = ThreadPoolExecutor(max_workers=10)
        # Since the API allows to fetch 20 results at a time, we're gonna repeat the fetch to get 100 records
        for res_key in range(0, 101, 20):
            executer.submit(retrieve_restaurant, lat, lon, cuisines_dict.get(cuisine), res_key,
                            restaurant_result_dictionary)
        executer.shutdown(wait=True)
        return restaurant_result_dictionary
	    
class VerifyLocation(Action):

    def __init__(self):
        self.TIER_1 = ['ahmedabad', 'bangalore', 'chennai',
                       'delhi', 'hyderabad', 'kolkata', 'mumbai', 'pune']
        self.TIER_2 = ['agra', 'ajmer', 'aligarh', 'allahabad', 'amravati', 'amritsar', 'asansol', 'aurangabad',
                       'bareilly', 'belgaum', 'bhavnagar', 'bhiwandi', 'bhopal', 'bhubaneswar', 'bikaner',
                       'bokaro steel city', 'chandigarh', 'coimbatore', 'cuttack', 'dehradun', 'dhanbad',
                       'durg-bhilai nagar', 'durgapur', 'erode', 'faridabad', 'firozabad', 'ghaziabad', 'gorakhpur',
                       'gulbarga', 'guntur', 'gurgaon', 'guwahati', 'gwalior', 'hubli', 'dharwad', 'indore', 'jabalpur',
                       'jaipur', 'jalandhar', 'jammu', 'jamnagar', 'jamshedpur', 'jhansi', 'jodhpur', 'kannur',
                       'kanpur', 'kakinada', 'kochi',
                       'kottayam', 'kolhapur', 'kollam', 'kota', 'kozhikode', 'kurnool', 'lucknow', 'ludhiana',
                       'madurai', 'malappuram', 'mathura', 'goa', 'mangalore', 'meerut', 'moradabad', 'mysore',
                       'nagpur', 'nanded', 'nashik', 'nellore', 'noida', 'palakkad', 'patna', 'pondicherry', 'raipur',
                       'rajkot', 'rajahmundry', 'ranchi', 'rourkela', 'salem', 'sangli', 'siliguri', 'solapur',
                       'srinagar', 'sultanpur', 'surat', 'thiruvananthapuram', 'thrissur', 'tiruchirappalli',
                       'tirunelveli', 'tiruppur', 'ujjain', 'vijayapura', 'vadodara', 'varanasi', 'vasai', 'virar',
                       'vijayawada', 'visakhapatnam', 'warangal']

    def name(self):
        return 'actions_VerifyLocation'

    def run(self, dispatcher, tracker, domain):
        location = tracker.get_slot('location')
        if not (self.verify_location(location)):
            dispatcher.utter_message(
                'We do not operate in ' + location + ' yet. Please try some other city.')
            return [SlotSet('location', None), SlotSet('location_ok', False)]
        else:
            return [SlotSet('location_ok', True)]

    def verify_location(self, location):
        return location.lower() in self.TIER_1 or location.lower() in self.TIER_2


class VerifyBudget(Action):

    def name(self):
        return 'actions_VerifyBudget'

    def run(self, dispatcher, tracker, domain):
        budget_criteria = tracker.get_slot('price')
        cost_min = 0
        cost_max = 1000

        error_msg = 'Sorry!! price range not supported, please re-enter.'
        try:
            if budget_criteria == 'low':
                cost_max = 300
            elif budget_criteria == 'mid':
                cost_min = 300
                cost_max = 700
            elif budget_criteria == 'high':
                cost_min = 700

        except ValueError:
            dispatcher.utter_message(error_msg)
            return [SlotSet('price', None), SlotSet('budget_ok', False)]
        min_dict = [0, 300, 700]
        max_dict = [300, 700]
        if cost_min in min_dict and (cost_max in max_dict or cost_max > 700):
            return [SlotSet('budget_ok', True)]
        else:
            dispatcher.utter_message(error_msg)
            return [SlotSet('price', None), SlotSet('budget_ok', False)]


class VerifyCuisine(Action):

    def name(self):
        return 'actions_VerifyCuisine'

    def run(self, dispatcher, tracker, domain):
        cuisines = ['bakery', 'biryani', 'cafe', 'chinese', 'mexican', 'italian', 'american', 'south indian',
                    'north indian']
        error_msg = 'Sorry!! The cuisine is not supported. Please re-enter.'
        cuisine = tracker.get_slot('cuisine')
        try:
            cuisine = cuisine.lower()
        except (RuntimeError, TypeError, NameError, AttributeError):
            dispatcher.utter_message(error_msg)
            return [SlotSet('cuisine', None), SlotSet('cuisine_ok', False)]
        if cuisine in cuisines:
            return [SlotSet('cuisine_ok', True)]
        else:
            dispatcher.utter_message(error_msg)
            return [SlotSet('cuisine', None), SlotSet('cuisine_ok', False)]


class ActionCalculateMealEstimate(Action):
    def name(self):
        return 'action_calculate_estimate'

    def run(self, dispatcher, tracker, domain):
        global meal_estimate
        people = int(tracker.get_slot('people').split(' ')[0])
        for restaurant in restaurant_email_list:
            restaurant_id = restaurant['restaurant']['id']
            try:
                if(people>1):
                    meal_estimate[restaurant_id] = (restaurant['restaurant']['average_cost_for_two']/2)*people
                    dispatcher.utter_message('your meal at '+ restaurant['restaurant']['name'] +' would cost approx. '+str(meal_estimate[restaurant_id]))
                else:
                    meal_estimate[restaurant_id] = restaurant['restaurant']['average_cost_for_two']/2
            except:
                meal_estimate[restaurant_id] = -1
        return []


class ActionSendEmail(Action):
    def name(self):
        return 'action_send_email'

    def run(self, dispatcher, tracker, domain):
        # Get user's email id
        to_email = tracker.get_slot('email')

        # Get location and cuisines to put in the email
        location = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        if tracker.get_slot('people'):
            people = tracker.get_slot('people').split(' ')[0]
        global restaurant_email_list, meal_estimate
        # Construct the email 'subject' and the contents.
        email_subject_line = 'You requested some ' + cuisine.capitalize() + ' restaurants in ' + str(location).capitalize()
        email_message_content = 'Hello ' + to_email.split('@')[0] + ',\n Here are the top ' + cuisine.capitalize() + ' restaurants in ' + str(location).capitalize() + '. \n \n'
        for index, restaurant in enumerate(restaurant_email_list):
            email_message_content += str(index + 1) + '. ' + restaurant['restaurant']['name'] + '\n'
            email_message_content += '\t Address : ' + restaurant['restaurant']['location']['address']+ '\n'
            email_message_content += '\t Timings : the restaurant is open from ' + restaurant['restaurant']['timings'] + '. \n'
            email_message_content += '\t The ratings are : ' + str(restaurant['restaurant']['user_rating']['aggregate_rating']) + '\n'
            email_message_content += '\t Here the average cost for 2 people is ' + restaurant['restaurant']['currency'] + str(restaurant['restaurant']['average_cost_for_two']) + '. \n'
            if(meal_estimate and len(meal_estimate)):
                email_message_content += '\t As per our chat you were going out with '+people+' people. So you\'ll be spending around '+ restaurant['restaurant']['currency'] + str(meal_estimate[restaurant['restaurant']['id']]) +'. \n'
            email_message_content += '\t Click this link to go to the location on maps : https://www.google.com/maps/@'+restaurant['restaurant']['location']['latitude']+','+restaurant['restaurant']['location']['longitude']+',15z \n \n'
        email_message_content = email_message_content+ '\n Please do let us know of your feedback by replying to this mail.\n'

        # Open SMTP connection to our email id.
        gmail_smtp = smtplib.SMTP('smtp.gmail.com', 587)
        gmail_smtp.starttls()
        gmail_smtp.login('superbotfoodie@gmail.com', 'iamarobot')

        # Create email message object
        email_message = EmailMessage()

        # Fill in message properties
        email_message['Subject'] = email_subject_line
        email_message['From'] = 'Foodie SuperBot'

        # Fill in the message content
        email_message.set_content(email_message_content)
        email_message['To'] = to_email

        gmail_smtp.send_message(email_message)
        gmail_smtp.quit()
        dispatcher.utter_message('I have sent you an email at ' + to_email)
        return []


def retrieve_restaurant(lat, lon, cuisine_id, res_key, restaurant_result_dictionary):
    base_url = 'https://developers.zomato.com/api/v2.1/'
    headers = {
        'Accept': 'application/json',
        'user-key': '5faeea4aac0526ad50539c0b87a5fd15'
    }
    params = {
        'lat': str(lat),
        'lon': str(lon),
        'cuisines': str(cuisine_id),
        'start': str(res_key),
        'count': 20
    }
    try:
        results = requests.get(base_url + 'search', params=params, headers=headers)
        results = results.json()
        restaurant_result_dictionary.extend(results['restaurants'])
    except Exception as e:
        print('An error occurred while fetching restaurants - ', e)
        return
