#Write an python code for chatbot for websites

# importing necessary libraries 
import random 
import re 

# list of responses 
responses = ["It's great to hear that!",
            "That's really interesting!",
            "That's awesome!",
            "That sounds fun!",
            "I'm glad to hear that!"] 

# function to respond to user input 
def respond(user_message): 
    # check for a greeting 
    if re.search(r"hi|hey|hello", user_message): 
        return random.choice(responses) 

    # check for a farewell 
    elif re.search(r"bye|farewell|see ya|good bye", user_message): 
        return "Bye! Have a great day!"

    # return a random response 
    else: 
        return random.choice(responses) 

# main 
while True: 
    user_message = input("\nEnter your message: ") 
    bot_response = respond(user_message) 
    print("Chatbot:", bot_response)