from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from const import (
    TOKEN,
)
from commands import (
    StartCommand,
    HelpCommand,
    ListCommand,
)
from conversation import conversation_handler
from message_responder import HandleMessage

# Main bot setting up
if __name__ == "__main__":
    print("bot started")
    application = ApplicationBuilder().token(TOKEN).build()
    # commands
    start_handler = CommandHandler("start", StartCommand)
    help_handler = CommandHandler("help", HelpCommand)
    list_handler = CommandHandler("list", ListCommand)

    # add the handelers
    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(list_handler)
    application.add_handler(conversation_handler)
    application.add_handler(MessageHandler(filters.TEXT, HandleMessage))
    # start polling
    application.run_polling()
