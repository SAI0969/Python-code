import os
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Your bot's API token (provided by BotFather)
API_TOKEN = '7489475122:AAEeqOUYWFdG9tlUzwrDtGO2uAtetjBA6Vw'


x = r"C:/Users/gayat/Downloads/Gitam Python"

# For listing the files
async def list_files(update: Update, context: CallbackContext):
    file_location = " ".join(context.args) if context.args else x
    
    
    if os.path.isdir(file_location):
        files = os.listdir(file_location)
        if files:
            file_list = "\n".join(files)
            await update.message.reply_text(f"Files and directories in '{file_location}':\n{file_list}")
        else:
            await update.message.reply_text(f"The directory '{file_location}' is empty.")
    else:
        await update.message.reply_text(f"No directory found at '{file_location}'.")


# For starting the bot
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Hello! I can check if a .txt file exists at a given location and I can upload it to you.\nClick /help to know how to use me.")
    
    
# For uploading
async def upload(update: Update, context: CallbackContext):
    file_location = " ".join(context.args) if context.args else x
    if os.path.isfile(file_location) and file_location.endswith(".txt"):
        await update.message.reply_document(file_location, caption=file_location)
    else:
        await update.message.reply_text(f"No .txt file found at '{file_location}'.")
   
# For /help
async def help(update: Update, context: CallbackContext):
    await update.message.reply_text("Gitam bot:\nNote the **** is the file name\nuse /list to get the total files that are present with me\nuse /upload ****.txt to get the file.")

def main():
   
    application = Application.builder().token(API_TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("upload", upload))
    application.add_handler(CommandHandler("list", list_files))
    application.add_handler(CommandHandler("help", help))

    application.run_polling()

if __name__ == '__main__':
    main()










