import logging
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# তোমার টোকেন আর চ্যানেল আইডি
BOT_TOKEN = 8258786899:AAGYHqWnl1NIkNm-nZb2ylWdrMjmqdQt7gw
CHANNEL_ID = -1002055880260  # তোমার চ্যানেল আইডি

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# /start কমান্ড
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("হ্যালো হৃদয় 💙 আমি তোমার মুভি সার্চ বট 🤖")

# মুভি খোঁজার সিস্টেম
async def search_movie(update: Update, context: CallbackContext):
    query = update.message.text
    # এখানে আসলে ডাটাবেস/চ্যানেল থেকে খোঁজা হবে
    # আপাতত ডেমো হিসেবে একটা বাটন পাঠাচ্ছি
    button = [[InlineKeyboardButton("Download ✅", url="https://t.me/YourChannel")]]
    await update.message.reply_text(f"🔎 খুঁজে পেলাম: {query}", reply_markup=InlineKeyboardMarkup(button))

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search_movie))

    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()