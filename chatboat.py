
import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses for the chatbot
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hey there!", "Hi! How can I help you today?"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm great, thanks for asking!", "I'm good, how about you?"]
    ],
    [
        r"(.*) your name ?",
        ["My name is ChatBot. What's yours?",]
    ],
    [
        r"what can you do ?",
        ["I can help you with general queries. Just ask me anything!",]
    ],
    [
        r"bye|goodbye",
        ["Goodbye!", "Bye! Have a great day!", "Take care!"]
    ],
]

# Create a Chat instance
chatbot = Chat(pairs, reflections)

def chat():
    print("Welcome! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("ChatBot: Goodbye!")
            break
        else:
            print("ChatBot:", chatbot.respond(user_input))

# Start the chat
if _name_ == "_main_":
    chat()
