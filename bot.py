from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


TOKEN = "5562164106:AAE2cjpILKLGVnR7HLtshnMk5o2GOZCAkTg"

def start(update, context):
    update.message.reply_text("🗡Benvenuto nella landa dei consiglieri🌎")

def rispondi(update, context):
    update.message.text.lower()
    update.message.reply_text("suca")

updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, rispondi))
print("Bot in ascolto...")
updater.start_polling()