import os
import os.path
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

load_dotenv()
API_TOKEN = os.environ.get("telegram_bot")


DEFAULT_PATH = r"C:/Users/gayat/Downloads/Gitam Python"

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Hello! I can check if a .txt file exists at a given location and upload it to you.\n"
        "Click /help to know how to use me."
    )

# Command: /help
async def help(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Gitam bot commands:\n"
        "/list- To view the files that you can get\n"
        "/upload filename.txt - Send a specific .txt file.\n"
        "/start - Start the bot.\n"
    )

async def list_files(update: Update, context: CallbackContext):
    file_location = " ".join(context.args) if context.args else DEFAULT_PATH

    if os.path.isdir(file_location):
        files = os.listdir(file_location)
        if files:
            file_list = "\n".join(files)
            await update.message.reply_text(
                f"Files and directories in '{file_location}':\n{file_list}"
            )
        else:
            await update.message.reply_text(f"The directory '{file_location}' is empty.")
    else:
        await update.message.reply_text(f"No directory found at '{file_location}'.")

async def upload(update: Update, context: CallbackContext):
    file_location = " ".join(context.args) if context.args else ""

    if not file_location:
        await update.message.reply_text("Please specify a file path. Example:\n/upload example.txt")
        return

    if not os.path.isabs(file_location):
        file_location = os.path.join(DEFAULT_PATH, file_location)

    if os.path.isfile(file_location) and file_location.endswith(".txt"):
        await update.message.reply_document(open(file_location, "rb"), caption=file_location)
    else:
        await update.message.reply_text(f"No .txt file found at '{file_location}'.")

def main():
    if not API_TOKEN:
        raise ValueError("API token not found. Make sure the 'telegram_bot' variable is set in the .env file.")

    application = Application.builder().token(API_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("list", list_files))
    application.add_handler(CommandHandler("upload", upload))

    application.run_polling()

if __name__ == "__main__":
    main()
