from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json
from concurrent.futures import ThreadPoolExecutor
import requests

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"5faeea4aac0526ad50539c0b87a5fd15"}
		zomato = zomatopy.initialize_app(config)
		# Get location from slot
		loc = tracker.get_slot('location')

		# Get cuisine from slot
		cuisine = tracker.get_slot('cuisine')
        # Get budget criteria from slot and set minimum cost and max cost
		budget_criteria = tracker.get_slot('price')
		cost_min = 0
		cost_max = 1000
		if(budget_criteria=='low'):
		    cost_max = 300
		elif(budget_criteria=='mid'):
		    cost_min = 300
		    cost_max = 700
		else:
		    cost_min=700
        
		results, lat, lon = self.get_additional_location_details(loc,zomato)

		if (results == 0):
		    # Zomato API could not find details for this location.
		    restaurant_exist = False
		    dispatcher.utter_message("Sorry, no results found in this location:("+ "\n")
		else:
		    d_rest = self.get_restaurants(lat, lon, cost_min, cost_max, cuisine)

            # Filter the results based on budget
		    d_budget = [d_rest_single for d_rest_single in d_rest if ((int(d_rest_single['restaurant']['average_cost_for_two']) > cost_min) & (
                int(d_rest_single['restaurant']['average_cost_for_two']) < cost_max))]
            # Sort the results according to the restaurant's rating
		    d_budget_rating_sorted = sorted(
                d_budget, key=lambda k: k['restaurant']['user_rating']['aggregate_rating'], reverse=True)

            # Build the response
		    response = ""
		    restaurant_exist = False
		    if len(d_budget_rating_sorted) == 0:
		        dispatcher.utter_message("Sorry, no results found :("+ "\n")
		    else:
                # Pick the top 5
		        d_budget_rating_top5 = d_budget_rating_sorted[:5]
		        global d_email_rest
		        d_email_rest = d_budget_rating_sorted[:10]
		        if(d_email_rest and len(d_email_rest) > 0):
		            restaurant_exist = True
		        for restaurant in d_budget_rating_top5:
		            response = response + restaurant['restaurant']['name'] + " in " + restaurant['restaurant']['location']['address'] + \
                        " has been rated " + \
                        restaurant['restaurant']['user_rating']['aggregate_rating'] + "\n" + "\n"
		        dispatcher.utter_message("Here are our picks!"+ "\n" + response)
		return [SlotSet('location', loc), SlotSet('restaurant_exist', restaurant_exist)]
    
	def get_additional_location_details(self, loc, zomato):
        # Get location details including latitude and longitude
	    location_detail = zomato.get_location(loc, 1)
	    d1 = json.loads(location_detail)
	    lat = 0
	    lon = 0
	    results = len(d1["location_suggestions"])
	    if (results > 0):
	        lat = d1["location_suggestions"][0]["latitude"]
	        lon = d1["location_suggestions"][0]["longitude"]
	    return results, lat, lon
    
	def get_restaurants(self, lat, lon, budgetmin, budgetmax , cuisine):
	    cuisines_dict = {'american': 1, 'chinese': 25, 'italian': 55,
                         'mexican': 73, 'north indian': 50, 'south indian': 85}
	    d_rest = []
	    executer = ThreadPoolExecutor(max_workers=10)
	    for res_key in range(0, 101, 20):
	        executer.submit(retrieve_restaurant, lat, lon, cuisines_dict, cuisine, res_key, d_rest)
	    executer.shutdown()
	    return d_rest
    
# 		zomato = zomatopy.initialize_app(config)
# 		loc = tracker.get_slot('location')
# 		cuisine = tracker.get_slot('cuisine')
# 		location_detail=zomato.get_location(loc, 1)
# 		d1 = json.loads(location_detail)
# 		print(d1)
# 		lat=d1["location_suggestions"][0]["latitude"]
# 		lon=d1["location_suggestions"][0]["longitude"]
# 		cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
# 		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5)
# 		d = json.loads(results)
# 		response=""
# 		if d['results_found'] == 0:
# 			response= "no results"
# 		else:
# 			for restaurant in d['restaurants']:
# 				response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+"\n"
# 		
# 		dispatcher.utter_message("-----"+response)
# 		return [SlotSet('location',loc)]
    
class ActionSendMail(Action):
	def name(self):
		return 'action_send_email'
		
	def run(self, dispatcher, tracker, domain):
		print('email sent')
		email_address = tracker.get_slot('email')
		dispatcher.utter_message("I have sent you an email at "+email_address)
		return

def retrieve_restaurant(lat, lon, cuisines_dict, cuisine, res_key, d_rest):
    base_url = "https://developers.zomato.com/api/v2.1/"
    headers = {'Accept': 'application/json',
                'user-key': '5787bb8301dd97fbe86ec40febf7e03b'}
    try:
        results = (requests.get(base_url + "search?" + "&lat=" + str(lat) + "&lon=" + str(lon) + "&cuisines=" + str(
            cuisines_dict.get(cuisine)) + "&start=" + str(res_key)+"&count=20", headers=headers).content).decode("utf-8")
    except:
        return
    d = json.loads(results)
    d_rest.extend(d['restaurants'])
