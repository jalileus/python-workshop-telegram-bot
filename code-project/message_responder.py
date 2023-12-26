from telegram.ext import (
    ContextTypes,
)
from telegram import Update


# Function to handle response for normal messages
def HandleResponse(text: str):
    new_text = text.lower()

    if "hello" in new_text or "hey" in new_text or "hi" in new_text:
        return "Hi there!\nplease use the command /help to understand how do i work"
    elif "thank you" in new_text:
        return "you're welcome!"
    elif "list" in new_text:
        return "sorry!, i did not understand, do you mean /list ?"
    elif "timecomplexity" in new_text:
        return "sorry!, i did not understand, do you mean /timecomplexity ?"
    elif "cancel" in new_text:
        return "there is nothing to cancel !"
    elif "spacecomplexity" in new_text:
        return "sorry!, i did not understand, do you mean /spacecomplexity ?"
    elif "def" in new_text:
        return "sorry!, i did not understand, do you mean /def ?"
    elif "gif" in new_text:
        return "sorry!, i did not understand, do you mean /gif ?"
    elif "code" in new_text:
        return "sorry!, i did not understand, do you mean /code ?"
    elif "start" in new_text:
        return "sorry!, i did not understand, do you mean /start ?"
    elif "help" in new_text:
        return "sorry!, i did not understand, do you mean /help ?"
    elif "time complexity" in new_text:
        return "if you want to know about time complexity, please use the command: /def"
    elif "space complexity" in new_text:
        return (
            "if you want to know about space complexity, please use the command: /def"
        )
    elif "case" in new_text:
        return "if you want to know about cases of time complexity, please use the command: /def"
    return "Sorry!, i don't understand your message, please try again or use the command /help for more information"


# Function to handle the messages sent by the user
async def HandleMessage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text: str = update.message.text
    respone: str = HandleResponse(text)
    await update.message.reply_text(respone)
