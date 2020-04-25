## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_goodbye
    - export

## location specified
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "a.t@gmail.com"}
    - slot{"email": "a.t@gmail.com"}
    - action_send_email
* thank
    - utter_welcome
    - utter_goodbye
    
## cuisine specified
* greet
    - utter_greet
* restaurant_search{"cuisine": "cafe"}
    - slot{"cuisine": "cafe"}
    - utter_ask_location
* restaurant_search{"location": "Nanded"}
    - slot{"location": "Nanded"}
    - action_search_restaurants
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "a.t@gmail.com"}
    - slot{"email": "a.t@gmail.com"}
    - action_send_email
* thank
    - utter_welcome
    - utter_goodbye

## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - utter_goodbye

## complete path 3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
* goodbye
    - utter_goodbye

## complete path 4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - export


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* stop

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - slot{"location": "mumbai"}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye
    
    
## happy_path
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* affirm
    - utter_goodbye


## interactive_story_1
* greet
    - utter_greet
* unknown
    - utter_default
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - slot{"location": "Chennai"}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - slot{"location": "Pune"}
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "agra"}
    - slot{"location": "agra"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - slot{"location": "agra"}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Lucknow"}
    - slot{"location": "Lucknow"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"location": "Lucknow"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "a.t@gmail.com"}
    - slot{"email": "a.t@gmail.com"}
    - action_send_email
* thank
    - utter_welcome

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - utter_ask_location
* restaurant_search{"location": "warangal"}
    - slot{"location": "warangal"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - slot{"location": "warangal"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "apz@reddit.com"}
    - slot{"email": "apz@reddit.com"}
    - action_send_email
* thank
    - utter_welcome

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Nagpur"}
    - slot{"location": "Nagpur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Andhra"}
    - slot{"cuisine": "Andhra"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "Nagpur"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "someone@gmail.com"}
    - slot{"email": "someone@gmail.com"}
    - action_send_email
* thank
    - utter_welcome

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - utter_ask_location
* restaurant_search{"location": "Sangli"}
    - slot{"location": "Sangli"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Asian"}
    - slot{"cuisine": "Asian"}
    - action_search_restaurants
    - slot{"location": "Sangli"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "qwerty@poiu.com"}
    - slot{"email": "qwerty@poiu.com"}
    - action_send_email
* thank
    - utter_welcome

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Agra"}
    - slot{"location": "Agra"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Arabian"}
    - slot{"cuisine": "Arabian"}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"location": "Agra"}
    - utter_ask_email_permission
* deny
    - utter_acknowledgement
    - utter_goodbye

## interactive_story_1
* restaurant_search{"location": "Ajmer"}
    - slot{"location": "Ajmer"}
    - utter_acknowledgement
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Awadhi"}
    - slot{"cuisine": "Awadhi"}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"location": "Ajmer"}
    - utter_ask_email_permission
* send_email{"email": "adt@gmail.com"}
    - slot{"email": "adt@gmail.com"}
    - action_send_email
* thank
    - utter_welcome

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"people": "6 people"}
    - utter_ask_location
* restaurant_search{"location": "aligarh"}
    - slot{"location": "aligarh"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "BBQ"}
    - slot{"cuisine": "BBQ"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "aligarh"}
    - utter_ask_email_permission
* deny
    - utter_acknowledgement
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "bakery"}
    - slot{"cuisine": "bakery"}
    - utter_ask_location
* restaurant_search{"location": "Aligarh"}
    - slot{"location": "Aligarh"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "Aligarh"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "chopper@hotmail.com"}
    - slot{"email": "chopper@hotmail.com"}
    - action_send_email
* thank
    - utter_welcome

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"people": "7 people"}
    - slot{"people": "7 people"}
    - utter_ask_location
* restaurant_search{"location": "Amravati"}
    - slot{"location": "Amravati"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Bengali"}
    - slot{"cuisine": "Bengali"}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"location": "Amravati"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "huejazz@something.com"}
    - slot{"email": "huejazz@something.com"}
    - action_send_email

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Burger"}
    - slot{"cuisine": "Burger"}
    - utter_ask_location
* restaurant_search{"location": "Belgaum"}
    - slot{"location": "Belgaum"}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - utter_ask_numberofpeople
* restaurant_search{"people": "3 people"}
    - slot{"people": "3 people"}
    - action_search_restaurants
    - slot{"location": "Belgaum"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "popo@xyz.com"}
    - slot{"email": "popo@xyz.com"}
    - action_send_email
* thank
    - utter_welcome

## interactive_story_1
* restaurant_search{"cuisine": "burger"}
    - slot{"cuisine": "burger"}
    - utter_ask_location
* restaurant_search{"location": "Nellor"}
    - slot{"location": "Nellor"}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - utter_ask_numberofpeople
* restaurant_search{"people": "1"}
    - slot{"people": "1"}
    - action_search_restaurants
    - slot{"location": "Nellor"}
    - utter_ask_email_permission
* deny
    - utter_acknowledgement
* thank
    - utter_welcome

## interactive_story_1
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Hamirpur"}
    - slot{"location": "Hamirpur"}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - utter_ask_numberofpeople
* restaurant_search{"people": "9 people"}
    - slot{"people": "9 people"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Desserts"}
    - slot{"cuisine": "Desserts"}
    - action_search_restaurants
    - slot{"location": "Hamirpur"}
    - utter_ask_email_permission
* deny
    - utter_acknowledgement
    - utter_goodbye
    
## interactive_story_1
* restaurant_search{"cuisine": "cafe"}
    - slot{"cuisine": "cafe"}
    - utter_ask_location
* restaurant_search{"location": "Jammu"}
    - slot{"location": "Jammu"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - utter_ask_numberofpeople
* restaurant_search{"people": "3 persons"}
    - slot{"people": "3 persons"}
    - action_search_restaurants
    - slot{"location": "Jammu"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "popup@somnewemail.com"}
    - slot{"email": "popup@somnewemail.com"}
    - action_send_email

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Vadodara"}
    - slot{"location": "Vadodara"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "arabian"}
    - slot{"cuisine": "arabian"}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - utter_ask_numberofpeople
* restaurant_search{"people": "8 persons"}
    - slot{"people": "8 persons"}
    - action_search_restaurants
    - slot{"location": "Vadodara"}
    - utter_ask_email_permission
* send_email{"email": "someone@mailbox.com"}
    - slot{"email": "someone@mailbox.com"}
    - action_send_email
* thank
    - utter_welcome

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Australian"}
    - slot{"cuisine": "Australian"}
    - utter_ask_location
* restaurant_search{"location": "Kannur"}
    - slot{"location": "Kannur"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - utter_ask_numberofpeople
* restaurant_search{"people": "5 persons"}
    - slot{"people": "5 persons"}
    - action_search_restaurants
    - slot{"location": "Kannur"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "new_email@gmail.com"}
    - slot{"email": "new_email@gmail.com"}
    - action_send_email
