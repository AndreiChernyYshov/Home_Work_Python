from credit import bot_token
from telegram import Bot
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
from bot_command import *

bot = Bot(bot_token)
updater = Updater(bot_token)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
start_choice_handler = MessageHandler(Filters.regex('^(Телефонный справочник|Заполнить резюме)$'), start_choice)

summary_handler = MessageHandler(Filters.text, start_choice)

phonebook_handler = MessageHandler(Filters.text, phonebook)
phonebook_choice_handler = MessageHandler(Filters.text, phonebook)
write_handler = MessageHandler(Filters.text, write)
write_do_handler = MessageHandler(Filters.text, write_do)
find_number_handler = MessageHandler(Filters.text, find_number)
find_number_do_handler = MessageHandler(Filters.text, find_number_do)

cancel_handler = CommandHandler('cancel', cancel)

conv_handler = ConversationHandler(
    entry_points=[start_handler],
    states={
        START_CHOICE: [phonebook_handler, summary_handler],
        PHONEBOOK: [phonebook_choice_handler],
        PHONEBOOK_CHOICE: [write_handler, find_number_handler],
        WRITE: [write_do_handler],
        WRITE_DO: [write_do_handler],
        FIND_NUMBER: [find_number_do_handler],
        FIND_NUMBER_DO: [find_number_do_handler]
    },
    fallbacks=[cancel_handler])

dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()
