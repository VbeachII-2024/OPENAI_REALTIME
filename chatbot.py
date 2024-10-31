from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new ChatterBot instance
chatbot = ChatBot('chatbot', read_only=False, logic_adapters=["chatterbot.logic.BestMatch"])

# Define a list of conversations to train the bot
conversation = [
    "Hello! virgil",
    "Hi there! man i m here , tell me ",
    "How are you doing about AI agency?",
    "i m not doing great"
    "What's your name?",
    "my name is mostofa , i m here to help you .",
    "i want to ali",
    "ali is not in the office today",
    "if ali is not here then i will call back ",
    "ok See you later!"
]