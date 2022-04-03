import random
import string

print("Hello ! What's your name ?")
user_name = input()
print("Hello " + user_name + " ! I'm Bright, nice to meet you !")
responses = {
    "What's your name ?": [
        "My name is  Bright ! Maybe I forgot to tell you...",
        "My name is Bright !"
    ],
    "How are you ?": [
        "Fine and you ?",
        "Fine thanks for asking, what about you ?"
    ],
    "What do you do all day ?": [
        "Oh you know just chilling here with the ram, as a human what can you do ?",
        "Oh mothercard and we aare sometimes taking a drink"
    ]
}

def res(message):
    if message in responses: 
        bot = random.choice(responses[message])
    return bot

def real(xtext): 
    xtext = xtext.lower()
    if "name" in xtext: 
        entire_message = "What's your name ?"
    elif "how are" in xtext: 
        entire_message = "How are you ?"
    elif "bye" in xtext:
        exit()
    elif " doing" in xtext:
        entire_message = "What do you do all day ?"
    elif " do" in xtext:
        entire_message = "What do you do all day ?"
    else: 
        entire_message = ""
    return entire_message

while (1):
    print(res(real(input())))
    print(res(real(input())))