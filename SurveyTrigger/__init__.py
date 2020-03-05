import datetime
import logging

import azure.functions as func

import pathlib

from telegram.ext import Updater
import random

import telegram
import json
from dotenv import load_dotenv
import os


def send_poll():
    load_dotenv()

    # apikey = os.getenv("TELEGRAM_TOKEN") #this was without azure functions
    #groupid = os.getenv("CHAT_ID")
    apikey = os.environ["TELEGRAM_TOKEN"]
    groupid = os.environ["CHAT_ID"]
    updater = Updater(token=apikey, use_context=True)

    # load all questions and pick a random one
    questions = {}
    with open(pathlib.Path(__file__).parent / 'questions.json', 'r') as f:
        # with open('questions.json', 'r') as f:
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


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    send_poll()
    print("Executed polling..")
    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
