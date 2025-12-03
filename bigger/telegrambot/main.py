from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from model import getResponse

# Constants
TOKEN: Final[str] = "YOUR-BOT-TOKEN"
BOT_USERNAME: Final[str] = "BOT-USER-NAME"


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello there! Nice to meet you.')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Just type something')


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command')


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error: {context.error}")


def handle_response(text: str) -> str:
    processed: str = text.lower()

    # if 'hello' in processed:
    #     return "Hey there!"
    # if 'hi' in processed:
    #     return "Hey there!"
    # if 'nonai' in processed:
    #     return "Ki go Maa"
    # if 'butum' in processed:
    #     return "Baba tumi?"
    # else:
    return getResponse(processed)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    # Log users
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}')

    response = handle_response(text)

    await update.message.reply_text(response)


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"{update} caused error: {context.error}")


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', help_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error_handler)

    print('Polling')
    app.run_polling(poll_interval=3)


if __name__ == "__main__":
    main()
