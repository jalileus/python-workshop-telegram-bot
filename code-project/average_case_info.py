from telegram.ext import (
    ConversationHandler,
    ContextTypes,
)
from telegram import Update


# Function returns the time complexity of some algorithm in the average case
async def GetAverageTimeComplexity(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_choice_algorithm = update.message.text
    if user_choice_algorithm == "Bubble Sort":
        await update.message.reply_text(
            "The average number of swaps for any random array is (N^2)/4, so the average case time complexity is O(N^2)."
        )
    elif user_choice_algorithm == "Merge Sort":
        await update.message.reply_text(
            "The merge sort performs the same number of operations regardless of the input array. "
            "It divides the array recursively into two subarrays of equal size which will create logN subarrays. "
            "Then it repeatedly merges two subarrays in sorted order, which take linear time. "
            "So, the overall complexity is O(N log N).\nBest case = worst case = average case = O(N logN)"
        )
    elif user_choice_algorithm == "Quick Sort":
        await update.message.reply_text(
            "There are many ways to avoid the worst case of quicksort, like choosing the element from the middle of the array as pivot, "
            "randomly generating a pivot for each subarray, selecting the median of the first, last, and middle element as pivot, etc. "
            "By using these methods, we can ensure equal partitioning, on average. Thus, "
            "quick sort's average case time complexity is O(NlogN)."
        )
    elif user_choice_algorithm == "Insertion Sort":
        await update.message.reply_text(
            "The average case time complexity of insertion sort is also O(N^2)."
        )
    elif user_choice_algorithm == "Selection Sort":
        await update.message.reply_text(
            "The algorithm iterates the unsorted subarray (N - 1) times, "
            "and, after every iteration, the size of the unsorted subarray reduces by one. "
            "Thus the total number of comparisons is (N - 1) + (N - 2) + (N - 3) + ........... + 1 "
            "which is N * (N - 1)/2. So, the time complexity is quadratic."
            "It performs the same number of comparisons for any given array of size N, "
            "so the worst, best, and average cases are equal. \n"
            "Worst Case = Best Case = Average Case = O(n^2)"
        )
    elif user_choice_algorithm == "Heap Sort":
        await update.message.reply_text(
            "On average, O(logN) time is required to fetch the smallest or largest element from the heap, "
            "and we have to fetch N elements. So overall time complexity of quicksort is O(NlogN). "
            "The order of time taken by quicksort is always the same irrespective of the array.\n"
            "Best case = Worst case = Average case = O(N log N) "
        )
    elif user_choice_algorithm == "Counting Sort":
        await update.message.reply_text(
            "The time complexity to iterate over each element in the given input is O(N). "
            "Then the algorithm iterates through the auxiliary array that contributes O(K) time complexity. "
            "So, the overall time complexity is O(N + K).\n"
            "Best case = worst case = average case = O(N + K).\n"
            "The time complexity of the counting sort is linear, "
            "but we can't use it if the range of input elements is large."
        )
    elif user_choice_algorithm == "Radix Sort":
        await update.message.reply_text(
            "Let K be the number of digits in the maximum element of the array and b be the base of "
            "array elements.The counting sort for a particular digit takes O(N + b) time, "
            "and the algorithm runs the counting sort for all the K digits. Therefore, the total "
            "time complexity is O(K * (N + b))\n"
            "best case = worst case = average case = O(K * (N + b))"
        )
    elif user_choice_algorithm == "Bucket Sort":
        await update.message.reply_text(
            "Bucket sort runs in linear time when the elements are spread randomly in the array "
            "(e.g., Given array is a permutation of size N), as long as the sum of the squares of the bucket sizes is linear "
            "in the total number of items, so average case = best case"
        )
    elif user_choice_algorithm == "Cancel":
        await update.message.reply_text(
            "the command has been canceled!\nstart again by calling: /example_command"
        )
        return ConversationHandler.END
    return ConversationHandler.END
