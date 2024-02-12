from telegram.ext import MessageHandler,filters,ContextTypes,CommandHandler,Application
from telegram import Update,ForceReply
import logging

#logging ig ?


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

logging.getLogger("httpx").setLevel(logging.WARNING)

async def start(update : Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """SEND A MESSAGE WHEN  THE COMMAND /start is ussed by the user"""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hii {user.mention_html()}!",
        reply_markup=ForceReply(selective=True)
    )

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends messae when help command is used by the user."""
    user = update.effective_user
    await update.message.reply_text("WASSUP BITCH, WHAT HELP DO YOU NEED????")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """echo the user messsage."""
    await update.message.reply_text(update.message.text)

async def welcomeUser(update: Update, context: ContextTypes.DEFAULT_TYPE,newuser : filters.StatusUpdate.NEW_CHAT_MEMBERS) -> None:
    
def main() -> None:
    """Start the bot."""
    #create the application and pass it your bot's token.
    application =Application.builder().token("6746620662:AAF2rLd8jyLDuAtOvIWnFKVEwcHA8ji-8yU").build()
    application.add_handler(CommandHandler("start",start))
    application.add_handler(CommandHandler("help",help))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()



# async def new_member(update: Update, context):
#     new_members = update.message.new_chat_members
#     for member in new_member:
#         print(f"New member Joined : {update} (ID : {member.ID})")
#     reply_text = Update.message.reply_text("")

# def main():
# #initializing the updater
#     updater= updater("6746620662:AAF2rLd8jyLDuAtOvIWnFKVEwcHA8ji-8yU", use_context=True)
#     dispatcher = Updater.initialize
