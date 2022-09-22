from credit import bot_token
from telegram import Bot
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
from bot_command import *

bot = Bot(bot_token)
updater = Updater(bot_token)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)

summary_handler = MessageHandler(Filters.regex('^(Заполнить резюме)$'), summary)
gender_handler = MessageHandler(Filters.regex('^(Мужчина|Женщина)$'), gender)
photo_handler = MessageHandler(Filters.photo, photo)
bio_handler = MessageHandler(Filters.text, bio)
video_handler = MessageHandler(Filters.video, video)
sp_handler = MessageHandler(Filters.regex('^(Пропустить)$'), skip_photo)
sb_handler = MessageHandler(Filters.regex('^(Пропустить)$'), skip_bio)
sv_handler = MessageHandler(Filters.regex('^(Пропустить)$'), skip_video)

phonebook_handler = MessageHandler(Filters.regex('^(Телефонный справочник)$'), phonebook)
write_handler = MessageHandler(Filters.regex('^(Записать номер)$'), write)
write_do_handler = MessageHandler(Filters.text, write_do)
find_number_handler = MessageHandler(Filters.regex('^(Найти номер|Найти имя)$'), find_number)
find_number_do_handler = MessageHandler(Filters.text, find_number_do)

cancel_handler = CommandHandler('cancel', cancel)

conv_handler = ConversationHandler(
    entry_points=[start_handler],
    states={
        0: [summary_handler, phonebook_handler],
        1: [write_handler, find_number_handler],
        2: [write_do_handler],
        3: [find_number_do_handler],
        4: [gender_handler],
        5: [photo_handler, sp_handler],
        6: [bio_handler, sb_handler],
        7: [video_handler, sv_handler]
    },
    fallbacks=[cancel_handler])

dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()
