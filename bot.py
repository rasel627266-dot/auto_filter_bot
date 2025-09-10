import logging
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# ====== CONFIG ======
BOT_TOKEN = "8258786899:AAGYHqWnl1NIkNm-nZb2ylWdrMjmqdQt7gw"
CHANNEL_ID = "-1002055880260"

# Pre-defined movie database (movie name: download link)
# এখানে আমরা Channel URL ব্যবহার করছি
MOVIE_DB = {
    "iron man": f"https://t.me/{CHANNEL_ID}",
    "avatar": f"https://t.me/{CHANNEL_ID}",
    "inception": f"https://t.me/{CHANNEL_ID}",
    "avengers": f"https://t.me/{CHANNEL_ID}",
    "joker": f"https://t.me/{CHANNEL_ID}",
    "spider man": f"https://t.me/{CHANNEL_ID}"
}

# ===================

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# /start কমান্ড
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "হ্যালো হৃদয় 💙 আমি তোমার মুভি সার্চ বট 🤖\nমুভি নাম লিখে খুঁজে দেখো!"
    )

# মুভি খোঁজার সিস্টেম
async def search_movie(update: Update, context: CallbackContext):
    query = update.message.text.lower()
    found = False

    for movie_name, link in MOVIE_DB.items():
        if movie_name in query:
            button = [[InlineKeyboardButton("Download ✅", url=link)]]
            await update.message.reply_text(
                f"🔎 খুঁজে পেলাম: {movie_name.title()}", 
                reply_markup=InlineKeyboardMarkup(button)
            )
            found = True
            break

    if not found:
        await update.message.reply_text(
            "😔 দুঃখিত, মুভি খুঁজে পাওয়া যায়নি। অন্য নাম চেষ্টা করো।"
        )

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search_movie))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()