from telegram.ext import ContextTypes, ConversationHandler
from telegram import Update


# Function to send definitions
async def GetDefinition(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_choice = update.message.text
    if user_choice == "Time Complexity":
        await update.message.reply_text(
            "Time complexity: a description of how much computer time is required to run an algorithm."
        )
    elif user_choice == "Space Complexity":
        await update.message.reply_text(
            "Space complexity: is the amount of memory used to run an algorithm."
        )
    elif user_choice == "Sorting Algorithm":
        await update.message.reply_text(
            "Sorting algorithm: in computer science, a sorting algorithm is an algorithm that puts elements of a list into an order(ascending(increasing order) or descending(decreasing order))."
        )
    elif user_choice == "Worst Case":
        await update.message.reply_text(
            "Worst case: is the maximum amount of time required of inputs of a given size."
        )
    elif user_choice == "Average Case":
        await update.message.reply_text(
            "Average case: is the average amount of time required of inputs of a given size."
        )
    elif user_choice == "Best Case":
        await update.message.reply_text(
            "Best case: is the best amount of time required of inputs of a given size."
        )
    elif user_choice == "Mathimatical Notation":
        await update.message.reply_text(
            "Mathematical notation: the time complexity and is generally expressed as a function of the size of the input since this function is generally difficult to compute exactly, and the running time for small inputs is usually not consequential, one commonly focuses on the behavior of the complexity when the input size increases—that is, the asymptotic behavior of the complexity. Therefore, the time complexity is commonly expressed using big O notation, typically O(n),O(n log (n)),O(2^n) etc... where n is the size in units of bits needed to represent the input. space complexity can also be expressed the same way"
        )
    elif user_choice == "Cancel":
        await update.message.reply_text(
            "the command has been canceled!\nstart again by calling: /example_command"
        )
        return ConversationHandler.END
    return ConversationHandler.END
