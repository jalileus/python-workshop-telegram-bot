from telegram.ext import ContextTypes, ConversationHandler
from telegram import ReplyKeyboardMarkup, Update
from const import (
    CHOOSINGALGORITHMSPACE,
    CHOOSINGDEFINITION,
    DEFINITIONS,
    CHOOSINGCASE,
    SORTINGTYPES,
    CASES,
    CHOOSINGCODE,
    CHOOSINGGIF,
)


# Start command
async def StartCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("the user called the command start")
    await update.message.reply_text(
        "Welcome to the sorting algorithm bot!, Thank you for Choosing me.\ni'll try my best to help you understand the time complexity "
        "and the space complexity of the most important sorting algorithms.\n"
        "i'm here also to show you the implementations of those algorithms, if it was hard to understand it, you can ask me to send you "
        "a gif for the sorting algorithm and you can see it yourself.\nis it still hard to understand what "
        "is the time complexity and the space complexity and what is the mathematical logic behind it?\nif it is then, i'll provide you with simple definitions "
        "all you have to do is to ask me!.\ni'll be so glad to help you!, i hope you will learn something new with me.\n"
        "please start with the command /help to know how do i work.\nwish you the best luck ^_^."
    )


# Help command
async def HelpCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("the user called the command help")
    await update.message.reply_text(
        "welcome to the help section, this is how to use the bot:\n"
        "type: /start, to start the bot.\n"
        "type: /def , and choose an item to know its definition and get informations about.\n"
        "type: /timecomplexity , and then choose one of the cases, after you do, choose one of the sorting algorithms available to know about its time complexity.\n"
        "type: /spacecomplexity , and choose one of the sorting algorithms available to know about its space complexity.\n"
        "type: /list , to see all the sorting algorithms available.\n"
        "type: /gif , and then choose one of the sorting algorithms to get a gif to visualize the algorithm.\n"
        "type: /code, and then choose one of the sorting algorithms to get a pseudocodes for the algorithm.\n"
        "you can also try to chat with the bot, for example you can say hello, try it yourself!, the bot will reply."
    )


# List command of sorting algorithms available
async def ListCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("the user called the command list")
    await update.message.reply_text(
        "here are the most important sorting algorithms: \n"
        "1.Bubble Sort \n"
        "2.Merge Sort \n"
        "3.Quick Sort \n"
        "4.Selection Sort \n"
        "5.Insertion Sort \n"
        "6.Heap Sort \n"
        "7.Counting Sort \n"
        "8.Radix Sort \n"
        "9.Bucket Sort \n"
    )


# Cancel command
async def Cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("the user canceled the last operation")
    await update.message.reply_text("canceled")
    return ConversationHandler.END


# Defenition command
async def DefCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("the user asked for definitons")
    definitions = DEFINITIONS
    await update.message.reply_text(
        "please choose one of the following definitions you want to know(scroll down for more)",
        reply_markup=ReplyKeyboardMarkup(definitions, one_time_keyboard=True),
    )
    return CHOOSINGDEFINITION


# Space compelxity command
async def SpaceComplexityCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("the user asked for space complexity")
    algorithms = SORTINGTYPES
    await update.message.reply_text(
        "please choose one of the following sorting algorithms to know about its space comlexity(scroll down for more)",
        reply_markup=ReplyKeyboardMarkup(algorithms, one_time_keyboard=True),
    )
    return CHOOSINGALGORITHMSPACE


# Time complexity command
async def TimeComplexityCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("the user asked for time complexity and he should choose a case")
    cases = CASES
    await update.message.reply_text(
        "please choose in which case you want to know about the time complexity of the sorting algorithm",
        reply_markup=ReplyKeyboardMarkup(cases, one_time_keyboard=True),
    )
    return CHOOSINGCASE


# Pseudocodes command
async def CodeCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("the user asked for codes")
    algorithms = SORTINGTYPES
    await update.message.reply_text(
        "please choose which sorting algorithm you want the code for(scroll down for more)",
        reply_markup=ReplyKeyboardMarkup(algorithms, one_time_keyboard=True),
    )
    return CHOOSINGCODE


# Gifs command
async def GifCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("the user asked for gifs")
    algorithms = SORTINGTYPES
    await update.message.reply_text(
        "please choose which sorting algorithm you want to see the visualization for(scroll down for more)",
        reply_markup=ReplyKeyboardMarkup(algorithms, one_time_keyboard=True),
    )
    return CHOOSINGGIF
