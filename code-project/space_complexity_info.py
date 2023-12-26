from telegram.ext import (
    ConversationHandler,
    ContextTypes,
)
from telegram import Update


# Function returns the space complexity of some algorithm
async def GetSpaceComplexity(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_choice = update.message.text
    if user_choice == "Bubble Sort":
        await update.message.reply_text(
            "The algorithm doesn't use any extra space other than the original array, so the space complexity is O(1)."
        )
    elif user_choice == "Merge Sort":
        await update.message.reply_text(
            "An extra array of size N is needed to store the merged array. Thus the space complexity is O(N)."
        )
    elif user_choice == "Quick Sort":
        await update.message.reply_text(
            "Unlike merge sort quicksort doesn't require any extra space "
            "to store arrays but additional memory is required for creating stack "
            "frames in recursive calls.So, the space complexity again depends on the pivot,"
            "for example If we select the largest or smallest elementas a pivot then the space complexity "
            "will be O(N), but If we manage to partitionthe array in equal halves each time the the space complexity will be O(N log N)."
        )
    elif user_choice == "Selection Sort":
        await update.message.reply_text(
            "The algorithm doesn't use any extra space, so the space complexity is constant."
        )
    elif user_choice == "Insertion Sort":
        await update.message.reply_text(
            "The algorithm doesn't use any extra space other than the original array, so the space complexity is O(1)."
        )
    elif user_choice == "Heap Sort":
        await update.message.reply_text(
            "Heap sort doesn't require extra space as it simply converts the given array into "
            "a heap.Therefore, its space complexity is O(1)."
        )
    elif user_choice == "Counting Sort":
        await update.message.reply_text(
            "The algorithm requires an auxiliary array of size K, so the space complexity is O(k)."
        )
    elif user_choice == "Radix Sort":
        await update.message.reply_text(
            "The space complexity of radix sort is the same as counting sort, which is O(N + K)."
        )
    elif user_choice == "Bucket Sort":
        await update.message.reply_text(
            "If K is the number of buckets required, then O(K) extra space is needed to store K empty buckets, "
            "and then we map each element to a bucket that requires O(N) extra space. So the overall space complexity is O(N + K)."
        )
    elif user_choice == "Cancel":
        await update.message.reply_text(
            "the command has been canceled!\nstart again by calling: /example_command"
        )
        return ConversationHandler.END
    return ConversationHandler.END
