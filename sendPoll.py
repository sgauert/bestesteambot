from telegram.ext import Updater
import random

import telegram
import json
from dotenv import load_dotenv
import os

load_dotenv()

apikey = os.getenv("TELEGRAM_TOKEN")
groupid = os.getenv("CHAT_ID")
updater = Updater(token=apikey, use_context=True)

# load all questions and pick a random one
questions = {}
with open('questions.json', 'r') as f:
    questions = json.load(f)


selectedQuestionIndex = random.randint(0, len(questions.keys())-1)
selectedQuestion = list(questions.keys())[selectedQuestionIndex]
selectedOptions = list(questions.values())[selectedQuestionIndex]

print("Loaded Question: ")
print(selectedQuestion)
print(str(selectedOptions))

# insert randomized weekly question
updater.bot.send_poll(
    chat_id=groupid, question=selectedQuestion, options=selectedOptions)
