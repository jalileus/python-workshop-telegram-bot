from telegram.ext import (
    CommandHandler,
    MessageHandler,
    filters,
    ConversationHandler,
)
from const import (
    CHOOSINGDEFINITION,
    CHOOSINGCASE,
    CHOOSINGALGORITHMSPACE,
    WORSTCASEANSWER,
    BESTCASEANSWER,
    AVERAGECASEANSWER,
    CHOOSINGCODE,
    CHOOSINGGIF,
)
from commands import (
    DefCommand,
    SpaceComplexityCommand,
    TimeComplexityCommand,
    Cancel,
    CodeCommand,
    GifCommand,
)
from pseudocodes import GetPseudoCode
from space_complexity_info import GetSpaceComplexity
from average_case_info import GetAverageTimeComplexity
from best_case_info import GetBestTimeComplexity
from worst_case_info import GetWorstTimeComplexity
from definitions import GetDefinition
from cases import GetCases
from visualization import GetGif

# Initializing the conversation handler
conversation_handler = ConversationHandler(
    # Additional commands
    entry_points=[
        CommandHandler("def", DefCommand),
        CommandHandler("timecomplexity", TimeComplexityCommand),
        CommandHandler("spacecomplexity", SpaceComplexityCommand),
        CommandHandler("code", CodeCommand),
        CommandHandler("gif", GifCommand),
    ],
    # States of answearing
    states={
        CHOOSINGDEFINITION: [
            MessageHandler(
                filters.Regex(
                    "^(Time Complexity|Space Complexity|Sorting Algorithm|Worst Case|Average Case|Best Case|Mathimatical Notation|Cancel)$"
                ),
                GetDefinition,
            ),
        ],
        CHOOSINGALGORITHMSPACE: [
            MessageHandler(
                filters.Regex(
                    "^(Bubble Sort|Merge Sort|Quick Sort|Selection Sort|Insertion Sort|Heap Sort|Counting Sort|Radix Sort|Bucket Sort|Cancel)$"
                ),
                GetSpaceComplexity,
            ),
        ],
        CHOOSINGCASE: [
            MessageHandler(
                filters.Regex("^(Best Case|Average Case|Worst Case|Cancel)$"), GetCases
            )
        ],
        WORSTCASEANSWER: [
            MessageHandler(
                filters.Regex(
                    "^(Bubble Sort|Merge Sort|Quick Sort|Selection Sort|Insertion Sort|Heap Sort|Counting Sort|Radix Sort|Bucket Sort|Cancel)$"
                ),
                GetWorstTimeComplexity,
            )
        ],
        BESTCASEANSWER: [
            MessageHandler(
                filters.Regex(
                    "^(Bubble Sort|Merge Sort|Quick Sort|Selection Sort|Insertion Sort|Heap Sort|Counting Sort|Radix Sort|Bucket Sort|Cancel)$"
                ),
                GetBestTimeComplexity,
            ),
        ],
        AVERAGECASEANSWER: [
            MessageHandler(
                filters.Regex(
                    "^(Bubble Sort|Merge Sort|Quick Sort|Selection Sort|Insertion Sort|Heap Sort|Counting Sort|Radix Sort|Bucket Sort|Cancel)$"
                ),
                GetAverageTimeComplexity,
            ),
        ],
        CHOOSINGCODE: [
            MessageHandler(
                filters.Regex(
                    "^(Bubble Sort|Merge Sort|Quick Sort|Selection Sort|Insertion Sort|Heap Sort|Counting Sort|Radix Sort|Bucket Sort|Cancel)$"
                ),
                GetPseudoCode,
            )
        ],
        CHOOSINGGIF: [
            MessageHandler(
                filters.Regex(
                    "^(Bubble Sort|Merge Sort|Quick Sort|Selection Sort|Insertion Sort|Heap Sort|Counting Sort|Radix Sort|Bucket Sort|Cancel)$"
                ),
                GetGif,
            )
        ],
    },
    # Set cancel command to fall back
    fallbacks=[CommandHandler("cancel", Cancel)],
)
