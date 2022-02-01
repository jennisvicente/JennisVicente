Chatbot Project:

NLU Training (40%)60/60
Feedback: good work
Intent Classification

Feedback: In this task 
you have to create a sufficient number of relevant, varied examples for intent classification.
Following steps should be done
1. You have to show the basic intents that bot must classify are Greet, Affirm, Deny, Restaurant search, Goodbye.
2. Train the model by running nlu_model.py and then run the script nlu.testing.py. This will give the intent score and score of different entities.
Was this helpful to you?
Entity Recognition

Feedback: In this task 
1. The NLU layer should be correctly able to recognise location.
2. The NLU layer should be correctly able to recognise cuisines.
3. The NLU layer should be correctly able to recognise budget.
4. The NLU layer should be correctly able to recognise email.
Was this helpful to you?
Dialogue Management -Training & Error Handling (45%)68/68
Feedback: good work
Conversational Flow

Feedback: In this task you have to 
Extract relevant entity from zomato API
You have to 
1. Built 'custom' action to fetch restaurant results using the required entities(location, cuisine, budget) given by the user.
2. Check the actions.py file for the same.
3. check whether the restaurants displayed should be sorted according to zomato user rating.
Was this helpful to you?
Conversational Flow -Stories

Feedback: In this task you have to

1.Built the vanilla conversation flow: where the bot ask question for each entity i.e., location, cuisine preference, average budget. It should display the top 5 restaurant for the given preferences in a sorted order(descending) of the average zomato user rating andthen ask the user whether he/she wants the details on email, and take action basis the user response.
2. Train the dialogue flow model for different patterns in dialogue flow.
Restaurant Results

Feedback: The output displayed / sent through mail should be relevant i.e., 
The model should display genuine results, i.e., when asked for Banglore, chinese cuisine and>700 budget, it shouldn't show results of some other location/cuisine/budget.
Also the result should be sorted in zomato rating.
Was this helpful to you?
Graceful error handling

Feedback: In this task you have to 
1. Train the model correctly to handle type 1 error: user enters a non existent/misspelt city preference
2. Train the model correctly to handle Type 2 error: user enters a city which is not included in tier-1 and tier-2 cities.
Send Mail (15%)22/22
Feedback: good work
Utterance Actions

Feedback: In this task you have to create the following 'email' utterance actions for the bot.

you have to 
1. Ask the user whether he wants the details of retaurant on email.
2. Ask the user for email address.
3. Acknowledge the user's response.
Sending Mail Action

Feedback: In this task you have to
 create a 'custom' action for sending mail to the required email id.

The mail should have the following details for each restaurant:
*Restaurant name.
*Restaurant lacality address.
*Average budget for two people.
*Zomato user rating.
