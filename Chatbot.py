import time
import random

responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "hello": ["Hi!", "Hello friend!", "Hey there!"],
    "whats your name": ["I'm Jeni!", "Call me MJ!", "My name is Jeni but you can call me MJ!"],
    "who made you": ["A student made me!", "I was created for a project!"],
    "bye": ["Goodbye!", "Bye bye!", "See you later!"],
    "how are you": ["I'm good!", "Doing fine!"],
    "thanks": ["You're welcome!", "No problem!"],
    "default": ["Sorry, I didnt understand", "Can you say that again?"]
    "good Morning":["HEY THERE GOOD MORNING!"]
}

def slow_print(message):
    for letter in message:
        print(letter, end='', flush=True)
        time.sleep(0.05)
    print()

def get_response(user_text):
    user_text = user_text.lower()
    
    for key in responses:
        if key in user_text:
            return random.choice(responses[key])
    
    return random.choice(responses["default"])

print("\nWelcome to Jeni (MJ) ChatBot!")
print("Type 'bye' to exit\n")
slow_print("Jeni: Hi! I'm Jeni (MJ for short). Lets chat!")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "bye":
        slow_print("Jeni: " + random.choice(responses["bye"]))
        break
    
    if user_input.strip() == "":
        slow_print("Jeni: Please type something...")
        continue
    
    bot_reply = get_response(user_input)
    slow_print("Jeni: " + bot_reply)

print("\nChat ended. Thanks for talking with me!")
