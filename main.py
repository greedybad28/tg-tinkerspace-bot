from telegram.ext import Updater,MessageHandler,filters
from telegram import Update
import logging

#logging ig ?


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

logging.getLogger("httpx").setLevel(logging.WARNING)




def new_member(update: Update, context):
    new_members = update.message.new_chat_members
    for member in new_member:
        print(f"New member Joined : {update} (ID : {member.ID})")
    reply_text = 

def main():
#initializing the updater
    updater= updater("6746620662:AAF2rLd8jyLDuAtOvIWnFKVEwcHA8ji-8yU", use_context=True)
    dispatcher = Updater.initialize
