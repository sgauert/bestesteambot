from telegram.ext import Updater
import telegram
from dotenv import load_dotenv
import os

load_dotenv()

apikey = os.getenv("TELEGRAM_TOKEN")
groupid = os.getenv("CHAT_ID")
updater = Updater(token=apikey, use_context=True)

# insert randomized weekly question
updater.bot.send_poll(chat_id=groupid, question="Hey y'all, mögt ihr mich?", options=[
                      "Sehr", "Nicht so sehr"])
