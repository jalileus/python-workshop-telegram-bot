from telegram.ext import (
    ConversationHandler,
    ContextTypes,
)
from telegram import Update


# Function to get pseudocodes of sorting algorithms
async def GetPseudoCode(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_choice = update.message.text
    if user_choice == "Bubble Sort":
        await update.message.reply_document("pseudocodes_assets/bubble_sort.txt")
    elif user_choice == "Merge Sort":
        await update.message.reply_document("pseudocodes_assets/merge_sort.txt")
    elif user_choice == "Quick Sort":
        await update.message.reply_document("pseudocodes_assets/quick_sort.txt")
    elif user_choice == "Selection Sort":
        await update.message.reply_document("pseudocodes_assets/selection_sort.txt")
    elif user_choice == "Insertion Sort":
        await update.message.reply_document("pseudocodes_assets/insertion_sort.txt")
    elif user_choice == "Heap Sort":
        await update.message.reply_document("pseudocodes_assets/heap_sort.txt")
    elif user_choice == "Counting Sort":
        await update.message.reply_document("pseudocodes_assets/counting_sort.txt")
    elif user_choice == "Radix Sort":
        await update.message.reply_document("pseudocodes_assets/radix_sort.txt")
    elif user_choice == "Bucket Sort":
        await update.message.reply_document("pseudocodes_assets/bucket_sort.txt")
    elif user_choice == "Cancel":
        await update.message.reply_text(
            "the command has been canceled!\nstart again by calling: /example_command"
        )
        return ConversationHandler.END
    return ConversationHandler.END
