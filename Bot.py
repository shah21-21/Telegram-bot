from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os

# Bot token
TOKEN = os.getenv("BOT_TOKEN")
# Group ID
GROUP_ID = 2856658181

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Message after /start
    message = "شماره خود را شیر کنید"
    # Glass button
    keyboard = [[InlineKeyboardButton("تایید هویت", request_contact=True)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(message, reply_markup=reply_markup)

async def handle_contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    contact = update.message.contact
    message_id = update.message.message_id
    chat_id = update.message.chat_id

    # Forward contact to group
    await context.bot.forward_message(chat_id=GROUP_ID, from_chat_id=chat_id, message_id=message_id)
    # Response to user
    await update.message.reply_text("پیگیری و در اسرع وقت با شما تماس گرفته خواهد شد")

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.CONTACT, handle_contact))

    application.run_polling()

if name == "main":
    main()
