import rules
from textblob import TextBlob

def handle_rule_check(user_input, rules):
    return rules[user_input]

while True:
    print("Hello, my name is Jarvis! How are you?")
    user_input = input().lower()
    blob = TextBlob(user_input)
    if blob.sentiment.polarity < 0:
        print("I'm sorry to hear that. Would you like to talk about it?")
    if blob.sentiment.polarity > 0.5:
        print("I'm happy to hear that, please tell me more!")
    # print(blob.sentiment)                                      only used to tell the emotional score of the input
    if user_input == "exit" or user_input == "goodbye" or user_input == "bye":
        print("Goodbye, have a wonderful day!")
        break
    if user_input not in rules.rules:
        print("Sorry, I don't understand that.")

    #response = handle_rule_check(user_input, rules.rules)
    #print(response)