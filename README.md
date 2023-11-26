# About python-workshop-telegram-bot:
This repository contains a Python project of a telegram bot, the repository contains two folders and one png file:

1. `pseudocode_assets` folder, contains all text file of the pseudocodes of the sorting algorithms.
2. `profile_photo.png` file, a photo file of the profile photo of the bot.
3. `code-project` folder, contains all the code scripts for the bot:

`main.py`(script used for setting up the bot(code runner))//`message_responder.py`(script used to handle responses for the messages sent by the user)//`conversation.py`(script used to initialize the conversation handler between the bot and the user to support multiple choosing and commands)//`visualization.py`(script used to send gifs of sorting algorithms depending on the user request after calling the command `/gif`)//`pseudocodes.py`(script used to send pseudocodes text files of sorting algorithms depending on the user request after calling the comman `/code`)//`commands.py`(script used to initialize 
all the commands of the bot like `/start` command `/help` command etc...)//`const.py`(script used to initialize and store all the constants required as `TOKEN`, `USERNAME` of the bot etc...)//`definitions.py`(script used to send the definitions available to the user after calling the command `/def` and choosing the definition required)//`space_complexity.py`(script used to send the space complexity of the sorting algorithms to the user after calling the command `/spacecomplexity` and choosing a sorting algorithm)//`cases.py`(script used to handle the choosing case and the algorithm after calling the command `/timecomplexity` by the user)//`best_case_info.py`, `average_case_info.py`, and `worst_case_info.py`(scripts used to send the time complexity of some algorithm depending on the choice of the case(best case, average case, or worst case) by the user).

# How to run:
1. you need to download `python-telegram-bot` version : `20.6`, for `Linux`: open the terminal and type the command: `sudo apt install python-telegram-bot`
for `Windows` open windows powershell and type the comand: `pip install python-telegram-bot`, `Note:` if you are facing a trouble downloading python telegram bot, have a look at the link: `https://pypi.org/project/python-telegram-bot/`.
2. after downloading python-telegram-bot you can run the `main.py` code in the platform you using preferably (Visual Studio 1.84.0) but it should work in any other plateforms.
3. after the running the code, go to telegram and search for the bot using the user name: `@EExxEEBoT_bot`.
4. press start, and start the code.
`Note`: the code prints some messages to the terminal when the user use the commands to help you understand, and let you know what is the user choosing or asking for in each step

# About the bot and how to use it:
the bot idea is to help the user undersatnd some concepts of programming such as time complexity, space complexity, and the most important sorting algorithms.
the bot support recognizing some kind of messages and can reply to it (hello, thank you, time complexity, space complexity, def, help, etc...), and in addition the code support the following commands:
1. `/start` command to start the bot.
2. `/help` command to get help the user with how to use the bot in a correct way.
3. `/list` command to send a list with all the possible algorithms available.
4. `/def` after the user click on the command /def a keyboard of choices will appear to the user, after choosing one of the concepts, the user will get its definition.
5. `/spacecomplexity`  after clicking on the command /spacecomplexity a keyboard of choices will appear, after choosing one of the algorithms, the user will get information about its space complexity.
6. `/timecomplexity` after clicking on the command /timecomplexity a keyboard of choices will appear, after choosing one of the cases the user wants, another keyboard will appear and the user can choose one of the sorting algorithms to get information about its time complexity
7. `/cancel` a command to cancel the most recent request.
8. `/code` after clicking on the command /code the user can choose one of the sorting algorithms, after that the bot will send a text file which contains a pseudocode of the algorithm choosen by the user.
9. `/gif` after clicking on the command /gif and choosing an algorithm, the bot will send the user a gif with a link of the source the bot took it from, so it will help the user to visualize the sorting algorithm required.
`Note:` the bot will send a message to inform the user to choose when you the user at the choosing state, otherwise, the bot will not understand the user choice without asking for the command(to inform the bot that the user want to start choosing).
