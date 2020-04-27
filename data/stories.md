## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Burger"}
    - slot{"cuisine": "Burger"}
    - actions_VerifyCuisine
    - slot{"cuisine": "Burger"}
    - slot{"cuisine_ok": true}
    - utter_ask_location
* restaurant_search{"location": "Belgaum"}
    - slot{"location": "Belgaum"}
    - actions_VerifyLocation
    - slot{"location": "Belgaum"}
    - slot{"location_ok": true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - actions_VerifyBudget
    - slot{"price": "low"}
    - slot{"budget_ok": true}
    - utter_ask_estimateCalculation
* affirm
    - utter_ask_numberofpeople
* restaurant_search{"people": "3 people"}
    - slot{"people": "3 people"}
    - action_search_restaurants
    - action_calculate_estimate
    - slot{"location": "Belgaum"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "popo@xyz.com"}
    - slot{"email": "popo@xyz.com"}
    - action_send_email
* thank
    - utter_welcome
    - utter_ask_howcanhelp

## interactive_story_1
* restaurant_search{"cuisine": "burger"}
    - slot{"cuisine": "burger"}
    - actions_VerifyCuisine
    - slot{"cuisine": "burger"}
    - slot{"cuisine_ok": true}
    - utter_ask_location
* restaurant_search{"location": "Nellor"}
    - slot{"location": "Nellor"}
    - actions_VerifyLocation
    - slot{"location": "Nellor"}
    - slot{"location_ok": true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - actions_VerifyBudget
    - slot{"price": "low"}
    - slot{"budget_ok": true}
    - utter_ask_estimateCalculation
* affirm
    - utter_ask_numberofpeople
* restaurant_search{"people": "1"}
    - slot{"people": "1"}
    - action_search_restaurants
    - action_calculate_estimate
    - slot{"location": "Nellor"}
    - utter_ask_email_permission
* deny
    - utter_acknowledgement
* thank
    - utter_welcome
    - utter_ask_howcanhelp

## interactive_story_1
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Hamirpur"}
    - slot{"location": "Hamirpur"}
    - actions_VerifyLocation
    - slot{"location": "Hamirpur"}
    - slot{"location_ok": true}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - actions_VerifyBudget
    - slot{"price": "high"}
    - slot{"budget_ok": true}
    - utter_ask_estimateCalculation
* affirm
    - utter_ask_numberofpeople
* restaurant_search{"people": "9 people"}
    - slot{"people": "9 people"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Desserts"}
    - slot{"cuisine": "Desserts"}
    - actions_VerifyCuisine
    - slot{"cuisine": "Desserts"}
    - slot{"cuisine_ok": true}
    - action_search_restaurants
    - action_calculate_estimate
    - slot{"location": "Hamirpur"}
    - utter_ask_email_permission
* deny
    - utter_acknowledgement
    - utter_goodbye
    - action_restart
    
## interactive_story_1
* restaurant_search{"cuisine": "cafe"}
    - slot{"cuisine": "cafe"}
    - actions_VerifyCuisine
    - slot{"cuisine": "cafe"}
    - slot{"cuisine_ok": true}
    - utter_ask_location
* restaurant_search{"location": "Jammu"}
    - slot{"location": "Jammu"}
    - actions_VerifyLocation
    - slot{"location": "Jammu"}
    - slot{"location_ok": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - actions_VerifyBudget
    - slot{"price": "high"}
    - slot{"budget_ok": true}
    - utter_ask_estimateCalculation
* affirm
    - utter_ask_numberofpeople
* restaurant_search{"people": "3 persons"}
    - slot{"people": "3 persons"}
    - action_search_restaurants
    - action_calculate_estimate
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
    - actions_VerifyLocation
    - slot{"location": "Vadodara"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "arabian"}
    - slot{"cuisine": "arabian"}
    - actions_VerifyCuisine
    - slot{"cuisine": "arabian"}
    - slot{"cuisine_ok": true}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - actions_VerifyBudget
    - slot{"price": "mid"}
    - slot{"budget_ok": true}
    - utter_ask_estimateCalculation
* affirm
    - utter_ask_numberofpeople
* restaurant_search{"people": "8 persons"}
    - slot{"people": "8 persons"}
    - action_search_restaurants
    - action_calculate_estimate
    - utter_ask_email_permission
* send_email{"email": "someone@mailbox.com"}
    - slot{"email": "someone@mailbox.com"}
    - action_send_email
* thank
    - utter_welcome
    - utter_ask_howcanhelp

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Australian"}
    - slot{"cuisine": "Australian"}
    - actions_VerifyCuisine
    - slot{"cuisine": "Australian"}
    - slot{"cuisine_ok": true}
    - utter_ask_location
* restaurant_search{"location": "Kannur"}
    - slot{"location": "Kannur"}
    - actions_VerifyLocation
    - slot{"location": "Kannur"}
    - slot{"location_ok": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - actions_VerifyBudget
    - slot{"price": "high"}
    - slot{"budget_ok": true}
    - utter_ask_estimateCalculation
* affirm
    - utter_ask_numberofpeople
* restaurant_search{"people": "5 persons"}
    - slot{"people": "5 persons"}
    - action_search_restaurants
    - action_calculate_estimate
    - slot{"location": "Kannur"}
    - actions_VerifyLocation
    - slot{"location": "Kannur"}
    - slot{"location_ok": true}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "new_email@gmail.com"}
    - slot{"email": "new_email@gmail.com"}
    - action_send_email

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Mysore"}
    - slot{"location": "Mysore"}
    - actions_VerifyLocation
    - slot{"location": "Mysore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "African"}
    - slot{"cuisine": "African"}
    - actions_VerifyCuisine
    - slot{"cuisine": "African"}
    - slot{"cuisine_ok": true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - actions_VerifyBudget
    - slot{"price": "low"}
    - slot{"budget_ok": true}
    - utter_ask_estimateCalculation
* affirm
    - utter_ask_numberofpeople
* restaurant_search{"people": "10 people"}
    - slot{"people": "10 people"}
    - action_search_restaurants
    - slot{"location": "Mysore"}
    - actions_VerifyLocation
    - slot{"location": "Mysore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* deny
    - utter_acknowledgement
* greet
    - utter_greet
* greet
    - utter_ask_howcanhelp
* restaurant_search{"location": "Aligarh"}
    - slot{"location": "Aligarh"}
    - actions_VerifyLocation
    - slot{"location": "Aligarh"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mughlai"}
    - slot{"cuisine": "Mughlai"}
    - actions_VerifyCuisine
    - slot{"cuisine": "Mughlai"}
    - slot{"cuisine_ok": true}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - actions_VerifyBudget
    - slot{"price": "mid"}
    - slot{"budget_ok": true}
    - utter_ask_estimateCalculation
* affirm
    - utter_ask_numberofpeople
* restaurant_search{"people": "14 friends"}
    - slot{"people": "14 friends"}
    - action_search_restaurants
    - action_calculate_estimate
    - slot{"location": "Aligarh"}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "myemail01.new@gmail.com"}
    - slot{"email": "myemail01.new@gmail.com"}
    - action_send_email
* thank
    - utter_welcome
    - utter_ask_howcanhelp
* greet
    - utter_greet
* greet
    - utter_greet

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bilaspur"}
    - slot{"location": "bilaspur"}
    - actions_VerifyLocation
    - slot{"location": "bilaspur"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - actions_VerifyCuisine
    - slot{"cuisine": "italian"}
    - slot{"cuisine_ok": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - actions_VerifyBudget
    - slot{"price": "high"}
    - slot{"budget_ok": true}
    - utter_ask_estimateCalculation
* affirm
    - utter_ask_numberofpeople
* restaurant_search{"people": "19 people"}
    - slot{"people": "19 people"}
    - action_search_restaurants
    - action_calculate_estimate
    - utter_ask_email_permission
* send_email{"email": "some12_.thing@someotherthing.com"}
    - slot{"email": "some12_.thing@someotherthing.com"}
    - action_send_email
* thank
    - utter_welcome
    - utter_ask_howcanhelp

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - actions_VerifyBudget
    - slot{"price": "high"}
    - slot{"budget_ok": true}
    - utter_ask_location
* restaurant_search{"location": "Bhiwandi"}
    - slot{"location": "Bhiwandi"}
    - actions_VerifyLocation
    - slot{"location": "Bhiwandi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - actions_VerifyCuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_ok": true}
    - utter_ask_estimateCalculation
* affirm
    - utter_ask_numberofpeople
* restaurant_search{"people": "5 people"}
    - slot{"people": "5 people"}
    - action_search_restaurants
    - action_calculate_estimate
    - utter_ask_email_permission
* deny
    - utter_acknowledgement
* thank
    - utter_welcome
    - utter_ask_howcanhelp

## interactive_story_1
* restaurant_search{"price": "low", "cuisine": "arabian", "location": "Bhilai", "people": "5 people"}
    - slot{"cuisine": "arabian"}
    - slot{"location": "Bhilai"}
    - slot{"people": "5 people"}
    - slot{"price": "low"}
    - action_search_restaurants
    - utter_ask_email_permission
* send_email{"email": "someemail123@sommailbox.com"}
    - slot{"email": "someemail123@sommailbox.com"}
    - action_send_email
* thank
    - utter_welcome
    - utter_ask_howcanhelp

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - actions_VerifyLocation
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - actions_VerifyLocation
    - slot{"location": "Pune"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Biryani"}
    - slot{"cuisine": "Biryani"}
    - actions_VerifyCuisine
    - slot{"cuisine": null}
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - actions_VerifyCuisine
    - slot{"cuisine": "italian"}
    - slot{"cuisine_ok": true}
    - utter_ask_estimateCalculation
* affirm
    - utter_ask_numberofpeople
* estimate_calculation{"people": "4 people"}
    - slot{"people": "4 people"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - actions_VerifyBudget
    - slot{"price": "high"}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - slot{"restaurant_exist": true}
    - action_calculate_estimate
    - utter_ask_email_permission
* affirm{"email": "this@that.com"}
    - slot{"email": "this@that.com"}
    - action_send_email
* thank
    - utter_welcome
    - utter_ask_howcanhelp

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - actions_VerifyLocation
    - slot{"location": "kolkata"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - actions_VerifyCuisine
    - slot{"cuisine": "italian"}
    - slot{"cuisine_ok": true}
    - utter_ask_estimateCalculation
* affirm
    - utter_ask_numberofpeople
* estimate_calculation{"people": "16 people"}
    - slot{"people": "16 people"}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - actions_VerifyBudget
    - slot{"price": "mid"}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "kolkata"}
    - slot{"restaurant_exist": true}
    - action_calculate_estimate
    - utter_ask_email_permission
* deny
    - utter_acknowledgement
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "high", "people": "5 people"}
    - slot{"people": "5 people"}
    - slot{"price": "high"}
    - actions_VerifyBudget
    - slot{"price": "high"}
    - slot{"budget_ok": true}
    - utter_ask_location
* restaurant_search{"location": "Italy"}
    - slot{"location": "Italy"}
    - actions_VerifyLocation
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - actions_VerifyLocation
    - slot{"location": "Chennai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Brazilian"}
    - slot{"cuisine": "Brazilian"}
    - actions_VerifyCuisine
    - slot{"cuisine": null}
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - actions_VerifyCuisine
    - slot{"cuisine": "italian"}
    - slot{"cuisine_ok": true}
    - action_search_restaurants
    - slot{"location": "Chennai"}
    - slot{"restaurant_exist": true}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "hithere@gothere.com"}
    - slot{"email": "hithere@gothere.com"}
    - action_send_email
* thank
    - utter_welcome
    - utter_ask_howcanhelp
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "America"}
    - slot{"location": "America"}
    - actions_VerifyLocation
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - actions_VerifyLocation
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - actions_VerifyCuisine
    - slot{"cuisine": "south indian"}
    - slot{"cuisine_ok": true}
    - utter_ask_estimateCalculation
* affirm
    - utter_ask_numberofpeople
* estimate_calculation{"people": "12 friends"}
    - slot{"people": "12 friends"}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - actions_VerifyBudget
    - slot{"price": "mid"}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"restaurant_exist": true}
    - action_calculate_estimate
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "yin@yang.com"}
    - slot{"email": "yin@yang.com"}
    - action_send_email
* thank
    - utter_welcome
    - utter_ask_howcanhelp
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "New York"}
    - slot{"location": "New York"}
    - actions_VerifyLocation
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - actions_VerifyLocation
    - slot{"location": "Delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - actions_VerifyCuisine
    - slot{"cuisine": "italian"}
    - slot{"cuisine_ok": true}
    - utter_ask_estimateCalculation
* affirm
    - utter_ask_numberofpeople
* estimate_calculation{"people": "6 people"}
    - slot{"people": "6 people"}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - actions_VerifyBudget
    - slot{"price": "low"}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"restaurant_exist": false}
* affirm

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "low", "cuisine": "australian", "location": "Australia", "people": "8 people"}
    - slot{"cuisine": "australian"}
    - slot{"location": "Australia"}
    - slot{"people": "8 people"}
    - slot{"price": "low"}
    - actions_VerifyCuisine
    - slot{"cuisine": null}
    - slot{"cuisine_ok": false}
    - actions_VerifyLocation
    - slot{"location": null}
    - slot{"location_ok": false}
    - actions_VerifyBudget
    - slot{"price": "low"}
    - slot{"budget_ok": true}
* restaurant_search{"cuisine": "Biryani", "location": "bangalore"}
    - slot{"cuisine": "Biryani"}
    - slot{"location": "bangalore"}
    - actions_VerifyCuisine
    - slot{"cuisine": "biryani"}
    - slot{"cuisine_ok": true}
    - actions_VerifyLocation
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - slot{"restaurant_exist": true}
    - utter_ask_email_permission
* send_email{"email": "a01.t@gmail.com"}
    - slot{"email": "a01.t@gmail.com"}
    - action_send_email
* thank
    - utter_welcome
    - utter_ask_howcanhelp

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "Delhi"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "Delhi"}
    - actions_VerifyCuisine
    - slot{"cuisine": "north indian"}
    - slot{"cuisine_ok": true}
    - actions_VerifyLocation
    - slot{"location": "Delhi"}
    - slot{"location_ok": true}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - actions_VerifyBudget
    - slot{"price": "mid"}
    - slot{"budget_ok": true}
    - utter_ask_estimateCalculation
* affirm
    - utter_ask_numberofpeople
* estimate_calculation{"people": "20 people"}
    - slot{"people": "20 people"}
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - action_calculate_estimate
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* unknown
    - utter_ask_email
* deny
    - utter_acknowledgement
* restaurant_search{"cuisine": "mexican", "location": "Belgaum"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Belgaum"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - utter_ask_estimateCalculation
* affirm
    - utter_ask_numberofpeople
* estimate_calculation{"people": "30 friends"}
    - slot{"people": "30 friends"}
    - action_search_restaurants
    - slot{"restaurant_exist": false}
* affirm
* thank
    - utter_welcome
    - utter_ask_howcanhelp
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "mid", "people": "9 people", "cuisine": "Brazillian", "location": "bangalore"}
    - slot{"cuisine": "Brazillian"}
    - slot{"location": "bangalore"}
    - slot{"people": "9 people"}
    - slot{"price": "mid"}
    - actions_VerifyCuisine
    - slot{"cuisine": null}
    - slot{"cuisine_ok": false}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - utter_ask_email_permission
* send_email{"email": "a@t.com"}
    - slot{"email": "a@t.com"}
    - action_send_email
* thank
    - utter_welcome
    - utter_ask_howcanhelp
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"price": "mid", "cuisine": "italian", "location": "bangalore"}
    - slot{"cuisine": "italian"}
    - slot{"location": "bangalore"}
    - slot{"price": "mid"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - utter_ask_estimateCalculation
* affirm
    - utter_ask_numberofpeople
* estimate_calculation{"people": "30 people"}
    - slot{"people": "30 people"}
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - action_calculate_estimate
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "a@t.com"}
    - slot{"email": "a@t.com"}
    - action_send_email
* thank
    - utter_welcome
    - utter_ask_howcanhelp

## interactive_story_1
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Germany"}
    - slot{"location": "Germany"}
    - actions_VerifyLocation
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "australia"}
    - slot{"location": "australia"}
    - actions_VerifyLocation
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "Agra"}
    - slot{"location": "Agra"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - utter_ask_estimateCalculation
* affirm
    - utter_ask_numberofpeople
* estimate_calculation{"people": "0"}
    - slot{"people": "0"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - action_calculate_estimate
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "a@t.com"}
    - slot{"email": "a@t.com"}
    - action_send_email
* thank
    - utter_welcome
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"price": "mid", "location": "Dharwar"}
    - slot{"location": "Dharwar"}
    - slot{"price": "mid"}
    - actions_VerifyLocation
    - slot{"location": null}
    - slot{"location_ok": false}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "arabian"}
    - slot{"cuisine": "arabian"}
    - actions_VerifyCuisine
    - slot{"cuisine": null}
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - utter_ask_estimateCalculation
* affirm
    - utter_ask_numberofpeople
* deny{"people": "0"}
    - slot{"people": "0"}
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - action_calculate_estimate
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "a@t.com"}
    - slot{"email": "a@t.com"}
    - action_send_email
* thank
    - utter_welcome
    - utter_ask_howcanhelp
* restaurant_search{"location": "Hubli"}
    - slot{"location": "Hubli"}
    - actions_VerifyLocation
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "Ajmer"}
    - slot{"location": "Ajmer"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - utter_ask_estimateCalculation
* affirm
    - utter_ask_numberofpeople
* estimate_calculation{"people": "0"}
    - slot{"people": "0"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - action_calculate_estimate
    - utter_ask_email_permission
* affirm
    - action_send_email
* thank
    - utter_welcome
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mysore"}
    - slot{"location": "Mysore"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - utter_ask_estimateCalculation
* affirm
    - utter_ask_numberofpeople
* estimate_calculation{"people": "5"}
    - slot{"people": "5"}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - action_calculate_estimate
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "a@t.com"}
    - slot{"email": "a@t.com"}
    - action_send_email
* thank
    - utter_welcome
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "high", "location": "Bijnor"}
    - slot{"location": "Bijnor"}
    - slot{"price": "high"}
    - actions_VerifyLocation
    - slot{"location": null}
    - slot{"location_ok": false}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
* restaurant_search{"location": "thiruvananthapuram"}
    - slot{"location": "thiruvananthapuram"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - utter_ask_estimateCalculation
* affirm
    - utter_ask_numberofpeople
* estimate_calculation{"people": "3"}
    - slot{"people": "3"}
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - action_calculate_estimate
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "a@t.com"}
    - slot{"email": "a@t.com"}
    - action_send_email
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "hubli-dharwad"}
    - slot{"location": "hubli-dharwad"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - utter_ask_estimateCalculation
* affirm
    - utter_ask_numberofpeople
* restaurant_search{"people": "9 people"}
    - slot{"people": "9 people"}
    - action_search_restaurants
    - action_calculate_estimate
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* affirm{"email": "s@t.com"}
    - slot{"email": "s@t.com"}
    - action_send_email
* thank
    - utter_welcome
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - utter_ask_location
* restaurant_search{"location": "hubli-dharwad"}
    - slot{"location": "hubli-dharwad"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - utter_ask_estimateCalculation
* affirm
    - utter_ask_numberofpeople
* estimate_calculation{"people": "7"}
    - slot{"people": "7"}
    - action_search_restaurants
    - action_calculate_estimate
    - utter_ask_email_permission
* deny
    - utter_acknowledgement
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bokaro steel city"}
    - slot{"location": "bokaro steel city"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - utter_ask_estimateCalculation
* affirm
    - utter_ask_numberofpeople
* estimate_calculation{"people": "8"}
    - slot{"people": "8"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - action_calculate_estimate
    - utter_ask_email_permission
* send_email{"email": "anshuman01.tripathi@gmail.com"}
    - slot{"email": "anshuman01.tripathi@gmail.com"}
    - action_send_email
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "durg-bhilai nagar"}
    - slot{"location": "durg-bhilai nagar"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Biryani"}
    - slot{"cuisine": "Biryani"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - utter_ask_estimateCalculation
* affirm
    - utter_ask_numberofpeople
* restaurant_search{"people": "9 friends"}
    - slot{"people": "9 friends"}
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - action_calculate_estimate
    - utter_ask_email_permission
* send_email{"email": "anshuman01.tripathi@gmail.com"}
    - slot{"email": "anshuman01.tripathi@gmail.com"}
    - action_send_email
* thank
    - utter_welcome
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "cafe"}
    - slot{"cuisine": "cafe"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - utter_ask_location
* restaurant_search{"location": "vasai-virar city"}
    - slot{"location": "vasai-virar city"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - utter_ask_estimateCalculation
* affirm
    - utter_ask_numberofpeople
* restaurant_search{"people": "12 freinds"}
    - slot{"people": "12 freinds"}
    - action_search_restaurants
    - slot{"restaurant_exist": false}
* affirm
* thank
    - utter_welcome
    - utter_ask_howcanhelp
* affirm
* restaurant_search{"location": "vasai-virar city"}
    - slot{"location": "vasai-virar city"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - action_calculate_estimate
    - utter_ask_email_permission
* send_email{"email": "anshuman01.tripathi@gmail.com"}
    - slot{"email": "anshuman01.tripathi@gmail.com"}
    - action_send_email
* restaurant_search{"location": "vasai-virar city"}
    - slot{"location": "vasai-virar city"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - action_search_restaurants
    - slot{"restaurant_exist": false}
* thank
    - utter_welcome
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "bakery", "location": "Lucknow"}
    - slot{"cuisine": "bakery"}
    - slot{"location": "Lucknow"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - utter_ask_estimateCalculation
* deny
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - utter_ask_email_permission
* deny
    - utter_acknowledgement
    - utter_ask_howcanhelp
* restaurant_search{"location": "kozhikode"}
    - slot{"location": "kozhikode"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"restaurant_exist": false}
* affirm
* thank
    - utter_welcome
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - utter_ask_estimateCalculation
* deny
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - utter_ask_email_permission
* deny
    - utter_acknowledgement
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "dharwad"}
    - slot{"location": "dharwad"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - utter_ask_estimateCalculation
* deny
    - utter_acknowledgement
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - utter_ask_email_permission
* send_email{"email": "anshuman01.tripathi@gmail.com"}
    - slot{"email": "anshuman01.tripathi@gmail.com"}
    - action_send_email
* thank
    - utter_welcome
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Guwahati"}
    - slot{"location": "Guwahati"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - utter_ask_estimateCalculation
* affirm
    - utter_ask_numberofpeople
* estimate_calculation{"people": "12"}
    - slot{"people": "12"}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - action_calculate_estimate
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "anshuman01.tripathi@gmail.com"}
    - slot{"email": "anshuman01.tripathi@gmail.com"}
    - action_send_email
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* unknown
    - utter_default
* unknown
    - utter_default
* unknown
    - utter_default
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bhiwandi"}
    - slot{"location": "Bhiwandi"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - utter_ask_estimateCalculation
* deny
    - utter_acknowledgement
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"restaurant_exist": false}
* affirm
* thank
    - utter_welcome
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
    - action_restart

## interactive_story_2
* greet
    - utter_greet
* unknown
    - utter_default
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bhiwandi"}
    - slot{"location": "bhiwandi"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - utter_ask_estimateCalculation
* deny
    - utter_acknowledgement
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - utter_ask_email_permission
* deny
    - utter_acknowledgement
    - utter_ask_howcanhelp
* estimate_calculation
    - utter_ask_numberofpeople
* restaurant_search{"people": "8 people"}
    - slot{"people": "8 people"}
    - action_calculate_estimate
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "anshuman01.tripathi@gmail.com"}
    - slot{"email": "anshuman01.tripathi@gmail.com"}
    - action_send_email
* thank
    - utter_welcome
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"people": "6 people"}
    - slot{"people": "6 people"}
    - utter_ask_location
* restaurant_search{"location": "jaisalmer"}
    - slot{"location": "jaisalmer"}
    - actions_VerifyLocation
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "jalandhar"}
    - slot{"location": "jalandhar"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - utter_ask_estimateCalculation
* affirm
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - action_calculate_estimate
    - utter_ask_email_permission
* deny
    - utter_acknowledgement
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "kanpur"}
    - slot{"location": "kanpur"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Biryani", "people": "4 people"}
    - slot{"cuisine": "Biryani"}
    - slot{"people": "4 people"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - utter_ask_estimateCalculation
* affirm
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - action_calculate_estimate
    - utter_ask_email_permission
* send_email{"email": "anshuman01.tripathi@gmail.com"}
    - slot{"email": "anshuman01.tripathi@gmail.com"}
    - action_send_email
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* unknown
    - utter_default
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "ludhiana"}
    - slot{"location": "ludhiana"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - utter_ask_estimateCalculation
* deny
    - utter_acknowledgement
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "anshuman01.tripathi@gmail.com"}
    - slot{"email": "anshuman01.tripathi@gmail.com"}
    - action_send_email
* thank
    - utter_welcome
    - utter_ask_howcanhelp
* estimate_calculation
    - utter_ask_numberofpeople
* estimate_calculation{"people": "10 people"}
    - slot{"people": "10 people"}
    - action_calculate_estimate
    - utter_ask_email_permission
* affirm
    - action_send_email
* thank
    - utter_welcome
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Kannur"}
    - slot{"location": "Kannur"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - utter_ask_estimateCalculation
* deny
    - utter_acknowledgement
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"restaurant_exist": false}
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - utter_ask_estimateCalculation
* deny
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "anshuman01.tripathi@gmail.com"}
    - slot{"email": "anshuman01.tripathi@gmail.com"}
    - action_send_email
* estimate_calculation
    - utter_ask_numberofpeople
* restaurant_search{"people": "15 people"}
    - slot{"people": "15 people"}
    - action_calculate_estimate
    - utter_ask_email_permission
* affirm
    - action_send_email
* thank
    - utter_welcome
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* unknown
    - utter_default
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Kanpur", "cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Kanpur"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - utter_ask_estimateCalculation
* affirm
    - utter_ask_numberofpeople
* restaurant_search{"people": "4 friends"}
    - slot{"people": "4 friends"}
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - action_calculate_estimate
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "anshuman01.tripathi@gmail.com"}
    - slot{"email": "anshuman01.tripathi@gmail.com"}
    - action_send_email
* thank
    - utter_welcome
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - utter_ask_location
* restaurant_search{"location": "Chandigarh"}
    - slot{"location": "Chandigarh"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - utter_ask_estimateCalculation
* deny
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - utter_ask_email_permission
* deny
    - utter_acknowledgement
    - utter_ask_howcanhelp
* estimate_calculation
    - utter_ask_numberofpeople
* restaurant_search{"people": "8 people"}
    - slot{"people": "8 people"}
    - action_calculate_estimate
    - utter_ask_email_permission
* deny
    - utter_acknowledgement
* thank
    - utter_welcome
    - utter_ask_howcanhelp
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Amritsar"}
    - slot{"location": "Amritsar"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - utter_ask_estimateCalculation
* deny
    - utter_acknowledgement
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "anshuman01.tripathi@gmail.com"}
    - slot{"email": "anshuman01.tripathi@gmail.com"}
    - action_send_email
* thank
    - utter_welcome
    - utter_ask_howcanhelp
* estimate_calculation
    - utter_ask_numberofpeople
* estimate_calculation{"people": "9 people"}
    - slot{"people": "9 people"}
    - action_calculate_estimate
    - utter_ask_email_permission
* affirm
    - action_send_email
* thank
    - utter_welcome
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - utter_ask_estimateCalculation
* affirm
    - utter_ask_numberofpeople
* estimate_calculation{"people": "3"}
    - slot{"people": "3"}
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - action_calculate_estimate
    - utter_ask_email_permission
* send_email{"email": "anshuman01.tripathi@gmail.com"}
    - slot{"email": "anshuman01.tripathi@gmail.com"}
    - action_send_email
* thank
    - utter_welcome
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"people": "7 people"}
    - slot{"people": "7 people"}
    - utter_ask_location
* restaurant_search{"location": "amravati"}
    - slot{"location": "amravati"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - utter_ask_estimateCalculation
* affirm
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - action_calculate_estimate
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "anshuman01.tripathi@gmail.com"}
    - slot{"email": "anshuman01.tripathi@gmail.com"}
    - action_send_email
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "bakery"}
    - slot{"cuisine": "bakery"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - utter_ask_location
* restaurant_search{"location": "Aligarh"}
    - slot{"location": "Aligarh"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - utter_ask_estimateCalculation
* deny
    - utter_acknowledgement
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "anshuman01.tripathi@gmail.com"}
    - slot{"email": "anshuman01.tripathi@gmail.com"}
    - action_send_email
* estimate_calculation
    - utter_ask_numberofpeople
* estimate_calculation{"people": "5 people"}
    - slot{"people": "5 people"}
    - action_calculate_estimate
    - utter_ask_email_permission
* affirm
    - action_send_email
* thank
    - utter_welcome
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"people": "6 people"}
    - slot{"people": "6 people"}
    - utter_ask_location
* restaurant_search{"location": "aligarh"}
    - slot{"location": "aligarh"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "BBQ"}
    - slot{"cuisine": "BBQ"}
    - actions_VerifyCuisine
    - slot{"cuisine": null}
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - utter_ask_estimateCalculation
* deny
    - utter_acknowledgement
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"restaurant_exist": false}
* restaurant_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - action_search_restaurants
    - slot{"restaurant_exist": false}
* affirm
* thank
    - utter_welcome
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"location": "ajmer"}
    - slot{"location": "ajmer"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_acknowledgement
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Biryani"}
    - slot{"cuisine": "Biryani"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - utter_ask_estimateCalculation
* deny
    - utter_acknowledgement
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - utter_ask_email_permission
* deny
    - utter_acknowledgement
    - utter_ask_howcanhelp
* estimate_calculation
    - utter_ask_numberofpeople
* estimate_calculation{"people": "5 people"}
    - slot{"people": "5 people"}
    - action_calculate_estimate
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "anshuman01.tripathi@gmail.com"}
    - slot{"email": "anshuman01.tripathi@gmail.com"}
    - action_send_email
* thank
    - utter_welcome
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "agra"}
    - slot{"location": "agra"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "arabian"}
    - slot{"cuisine": "arabian"}
    - actions_VerifyCuisine
    - slot{"cuisine": null}
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - utter_ask_estimateCalculation
* deny
    - utter_acknowledgement
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - utter_ask_email_permission
* deny
    - utter_acknowledgement
    - utter_ask_howcanhelp
* estimate_calculation
    - utter_ask_numberofpeople
* restaurant_search{"people": "4"}
    - slot{"people": "4"}
    - action_calculate_estimate
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "anshuman01.tripathi@gmail.com"}
    - slot{"email": "anshuman01.tripathi@gmail.com"}
    - action_send_email
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "awadhi", "location": "Ajmer", "price": "low"}
    - slot{"cuisine": "awadhi"}
    - slot{"location": "Ajmer"}
    - slot{"price": "low"}
    - actions_VerifyCuisine
    - slot{"cuisine": null}
    - slot{"cuisine_ok": false}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - utter_ask_estimateCalculation
* affirm
    - utter_ask_numberofpeople
* estimate_calculation{"people": "8"}
    - slot{"people": "8"}
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - action_calculate_estimate
    - utter_ask_email_permission
* deny
    - utter_acknowledgement
    - utter_ask_howcanhelp
* send_email
    - utter_ask_email
* send_email{"email": "anshuman01.tripathi@gmail.com"}
    - slot{"email": "anshuman01.tripathi@gmail.com"}
    - action_send_email
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"people": "7 people"}
    - slot{"people": "7 people"}
    - utter_ask_location
* restaurant_search{"location": "patiala"}
    - slot{"location": "patiala"}
    - actions_VerifyLocation
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "patna"}
    - slot{"location": "patna"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "BBQ"}
    - slot{"cuisine": "BBQ"}
    - actions_VerifyCuisine
    - slot{"cuisine": null}
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - utter_ask_estimateCalculation
* deny
    - utter_acknowledgement
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - utter_ask_email_permission
* deny
    - utter_acknowledgement
    - utter_ask_howcanhelp
* estimate_calculation
    - action_calculate_estimate
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "anshuman01.tripathi@gmail.com"}
    - slot{"email": "anshuman01.tripathi@gmail.com"}
    - action_send_email
* thank
    - utter_welcome
    - utter_ask_howcanhelp
* restaurant_search{"location": "bangalore", "cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bangalore"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - utter_ask_estimateCalculation
* affirm
    - utter_ask_numberofpeople
* estimate_calculation{"people": "7 people"}
    - slot{"people": "7 people"}
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - action_calculate_estimate
    - utter_ask_email_permission
* affirm
    - action_send_email
* send_email{"email": "someoneelse@something.com"}
    - slot{"email": "someoneelse@something.com"}
    - action_send_email
* thank
    - utter_welcome
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"people": "5"}
    - slot{"people": "5"}
    - utter_ask_location
* restaurant_search{"location": "raigarh"}
    - slot{"location": "raigarh"}
    - actions_VerifyLocation
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "Mysore"}
    - slot{"location": "Mysore"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - utter_ask_estimateCalculation
* deny
    - utter_acknowledgement
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - utter_ask_email_permission
* deny
    - utter_acknowledgement
    - utter_ask_howcanhelp
* estimate_calculation
    - action_calculate_estimate
    - utter_ask_email_permission
* deny
    - utter_acknowledgement
    - utter_ask_howcanhelp
* send_email
    - utter_ask_email
* send_email{"email": "anshuman01.tripathi@gmail.com"}
    - slot{"email": "anshuman01.tripathi@gmail.com"}
    - action_send_email
* thank
    - utter_welcome
    - utter_ask_howcanhelp
* goodbye
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "thiruvananthapuram"}
    - slot{"location": "thiruvananthapuram"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - utter_ask_estimateCalculation
* affirm
    - utter_ask_numberofpeople
* estimate_calculation{"people": "2"}
    - slot{"people": "2"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - action_calculate_estimate
    - utter_ask_email_permission
* deny
    - utter_acknowledgement
    - utter_ask_howcanhelp
* restaurant_search{"location": "kozhikode"}
    - slot{"location": "kozhikode"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_acknowledgement
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - utter_ask_estimateCalculation
* affirm
    - utter_ask_numberofpeople
* restaurant_search{"people": "4 people"}
    - slot{"people": "4 people"}
    - action_search_restaurants
    - slot{"restaurant_exist": false}
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - utter_ask_estimateCalculation
* affirm
    - utter_ask_numberofpeople
* estimate_calculation{"people": "5"}
    - slot{"people": "5"}
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - action_calculate_estimate
    - utter_ask_email_permission
* deny
    - utter_acknowledgement
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"people": "5 people", "location": "mysore"}
    - slot{"location": "mysore"}
    - slot{"people": "5 people"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - utter_ask_estimateCalculation
* affirm
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - action_calculate_estimate
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "meenakshy27i@gmail.com"}
    - slot{"email": "meenakshy27i@gmail.com"}
    - action_send_email
* thank
    - utter_welcome
    - utter_ask_howcanhelp
* affirm
* restaurant_search{"cuisine": "south indian", "location": "jammu"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "jammu"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - utter_ask_estimateCalculation
* deny
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - utter_ask_email_permission
* deny
    - utter_acknowledgement
    - utter_ask_howcanhelp
* unknown{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_default
* restaurant_search{"cuisine": "italian", "location": "gandhinagar"}
    - slot{"cuisine": "italian"}
    - slot{"location": "gandhinagar"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - actions_VerifyLocation
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "chandigarh"}
    - slot{"location": "chandigarh"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - utter_ask_estimateCalculation
* deny
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - utter_ask_email_permission
* deny
    - utter_acknowledgement
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - utter_ask_estimateCalculation
* deny
    - utter_acknowledgement
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* unknown
    - utter_ask_email
* unknown
    - utter_default
* send_email{"email": "meenakshy27i@gmail.com"}
    - slot{"email": "meenakshy27i@gmail.com"}
    - action_send_email
* thank
    - utter_welcome
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"cuisine": "icecream", "location": "bangalore"}
    - slot{"cuisine": "icecream"}
    - slot{"location": "bangalore"}
    - actions_VerifyCuisine
    - slot{"cuisine": null}
    - slot{"cuisine_ok": false}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - utter_ask_estimateCalculation
* affirm
    - utter_ask_numberofpeople
* deny
    - utter_acknowledgement
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "meenakshy27i@gmail.com"}
    - slot{"email": "meenakshy27i@gmail.com"}
    - action_send_email
* thank
    - utter_welcome
    - utter_ask_howcanhelp
* restaurant_search{"location": "itanagar"}
    - slot{"location": "itanagar"}
    - actions_VerifyLocation
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "agra", "cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "agra"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - utter_ask_estimateCalculation
* deny
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - utter_ask_email_permission
* affirm
    - action_send_email
* thank
    - utter_welcome
    - utter_ask_howcanhelp
* goodbye
    - utter_goodbye
    - action_restart


## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kalamassery"}
    - slot{"location": "kalamassery"}
    - actions_VerifyLocation
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "Ernakulam"}
    - slot{"location": "Ernakulam"}
    - actions_VerifyLocation
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "Kakkanad"}
    - slot{"location": "Kakkanad"}
    - actions_VerifyLocation
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "Kochi"}
    - slot{"location": "Kochi"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - utter_ask_estimateCalculation
* affirm
    - utter_ask_numberofpeople
* restaurant_search{"people": "5 persons"}
    - slot{"people": "5 persons"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - action_search_restaurants
    - slot{"restaurant_exist": false}
    - action_calculate_estimate
    - utter_ask_email_permission
* deny
    - utter_acknowledgement
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "price": "low"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "low"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - utter_ask_location
* restaurant_search{"location": "Palakkad"}
    - slot{"location": "Palakkad"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_estimateCalculation
* deny
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - utter_ask_email_permission
* affirm
    - utter_ask_email
* send_email{"email": "vivekav.96@gmail.com"}
    - slot{"email": "vivekav.96@gmail.com"}
    - action_send_email
* thank
    - utter_welcome
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"cuisine": "arabian"}
    - slot{"cuisine": "arabian"}
    - actions_VerifyCuisine
    - slot{"cuisine": null}
    - slot{"cuisine_ok": false}
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - actions_VerifyCuisine
    - slot{"cuisine_ok": true}
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - actions_VerifyLocation
    - slot{"location_ok": true}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - actions_VerifyBudget
    - slot{"budget_ok": true}
    - utter_ask_estimateCalculation
* affirm
    - utter_ask_numberofpeople
* restaurant_search{"people": "3 persons"}
    - slot{"people": "3 persons"}
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - action_calculate_estimate
    - utter_ask_email_permission
* deny
    - utter_acknowledgement
* thank
    - utter_welcome
    - utter_ask_howcanhelp
* deny
    - utter_goodbye
    - action_restart
