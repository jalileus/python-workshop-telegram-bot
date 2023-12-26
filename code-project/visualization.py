from telegram.ext import (
    ConversationHandler,
    ContextTypes,
)
from telegram import Update


# Function to get Gifs of sorting algorithms
async def GetGif(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_choice = update.message.text
    if user_choice == "Bubble Sort":
        await update.message.reply_animation(
            "https://i.imgur.com/Hcw3QS3.mp4", caption="https://imgur.com/gallery/omL5k"
        )
    elif user_choice == "Merge Sort":
        await update.message.reply_animation(
            "https://i.imgur.com/oMbHRV9.gif", caption="https://imgur.com/gallery/omL5k"
        )
    elif user_choice == "Quick Sort":
        await update.message.reply_animation(
            "https://i.imgur.com/GdAe2WF.gif", caption="https://imgur.com/gallery/omL5k"
        )
    elif user_choice == "Selection Sort":
        await update.message.reply_animation(
            "https://upload.wikimedia.org/wikipedia/commons/3/3e/Sorting_selection_sort_anim.gif?20220209224152",
            caption="https://commons.wikimedia.org/wiki/File:Sorting_selection_sort_anim.gif",
        )
    elif user_choice == "Insertion Sort":
        await update.message.reply_animation(
            "https://upload.wikimedia.org/wikipedia/commons/4/42/Insertion_sort.gif",
            caption="https://en.m.wikipedia.org/wiki/File:Insertion_sort.gif",
        )
    elif user_choice == "Heap Sort":
        await update.message.reply_animation(
            "https://i.imgur.com/CLGDr3I.gif", caption="https://imgur.com/gallery/omL5k"
        )
    elif user_choice == "Counting Sort":
        await update.message.reply_animation(
            "https://upload.wikimedia.org/wikipedia/commons/6/60/Counting_Sort_Animation.gif?20140818011201",
            caption="https://commons.wikimedia.org/wiki/File:Counting_Sort_Animation.gif",
        )
    elif user_choice == "Radix Sort":
        await update.message.reply_animation(
            "https://i.makeagif.com/media/7-17-2016/hlfsiC.gif",
            caption="https://makeagif.com/i/hlfsiC",
        )
    elif user_choice == "Bucket Sort":
        await update.message.reply_animation(
            "https://skilled.dev/images/bucket-sort.gif",
            caption="https://skilled.dev/course/sorting",
        )
    elif user_choice == "Cancel":
        await update.message.reply_text(
            "the command has been canceled!\nstart again by calling: /example_command"
        )
        return ConversationHandler.END
    return ConversationHandler.END
