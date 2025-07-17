import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable not set")

def start(update: Update, context: CallbackContext) -> None:
    args = context.args
    if args:
        encoded_url = args[0]
        original_url = encoded_url.replace('-', '/').replace('_', '.')
        update.message.reply_text(f"🎉 Here’s your free content:\n{original_url}")
    else:
        update.message.reply_text("👋 Welcome! You didn’t come through a content link.")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
  
