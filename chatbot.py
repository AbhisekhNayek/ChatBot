import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey!","Whats up!"]
    ],
    [
        r"how are you|how are things",
        ["I'm doing well, thank you. How about you?"]
    ],
    [
        r"(.*)good",
        ["That's great to hear!", "Awesome!", "Good to hear :)"]
    ],
    [
        r"(.*)bad",
        ["I'm sorry to hear that. What's been going on?", "That's too bad. Is there anything I can do to help?"]
    ],
    [
        r"(.*)help(.*)",
        ["Sure, what do you need help with?", "How can I assist you?"]
    ],
    [
        r"(.*)battery(.*)",
        ["Yes, my name is Battery! How can I help you today?"]
    ],
    [
        r"quit",
        ["Bye for now!", "Goodbye!", "Take care!"]
    ]
]

def battery_chatbot():
    print("Hi! My name is Battery. How can I help you today?")

    chatbot = Chat(pairs, reflections)
    chatbot.converse()

if __name__ == "__main__":
    battery_chatbot()
