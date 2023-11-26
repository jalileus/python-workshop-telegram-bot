from telegram.ext import ContextTypes, ConversationHandler
from telegram import ReplyKeyboardMarkup, Update
from const import (
    WORSTCASEANSWER,
    AVERAGECASEANSWER,
    BESTCASEANSWER,
    SORTINGTYPES,
)


# Function to choose the cases
async def GetCases(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("the user is choosing an algorithm")
    algorithms = SORTINGTYPES
    user_choice_case = update.message.text
    if user_choice_case == "Worst Case":
        print("the user chose worst case")
        await update.message.reply_text(
            "please choose an algorithm",
            reply_markup=ReplyKeyboardMarkup(algorithms, one_time_keyboard=True),
        )
        return WORSTCASEANSWER
    elif user_choice_case == "Average Case":
        print("the user chose average case")
        ConversationHandler.END
        await update.message.reply_text(
            "please choose an algorithm",
            reply_markup=ReplyKeyboardMarkup(algorithms, one_time_keyboard=True),
        )
        return AVERAGECASEANSWER
    elif user_choice_case == "Best Case":
        print("the user chose best case")

        await update.message.reply_text(
            "please choose an algorithm",
            reply_markup=ReplyKeyboardMarkup(algorithms, one_time_keyboard=True),
        )
        return BESTCASEANSWER
    elif user_choice_case == "Cancel":
        await update.message.reply_text(
            "the command has been canceled!\nstart again by calling: /example_command"
        )
        return ConversationHandler.END
    return ConversationHandler.END
