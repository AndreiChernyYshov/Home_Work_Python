from telegram.ext import ConversationHandler
from telegram import ReplyKeyboardMarkup
from data import *


def start(update, context):
    reply_keyboard = [['Телефонный справочник', 'Заполнить резюме']]
    update.message.reply_text('Выберите функцию: ',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return 0


def summary(update, context):
    reply_keyboard = [['Мужчина', 'Женщина']]
    update.message.reply_text('Добрый день!\nУкажите свой пол: ',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return 4


def gender(update, context):
    reply_keyboard = [['Пропустить']]
    update.message.reply_text('Отправьте фото, либо кнопку "Пропустить" для пропуска шага',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return 5


def photo(update, context):
    user = str(update.message.from_user['username'])
    photo_file = update.message.photo[-1].get_file()
    photo_file.download(f'{user}_photo.jpg')
    reply_keyboard = [['Пропустить']]
    update.message.reply_text('Отправьте свое резюме, либо кнопку "Пропустить" для пропуска шага',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return 6


def bio(update, context):
    user = str(update.message.from_user['username'])
    with open(user + '_bio.txt', 'w') as f:
        f.write(update.message.text)
    reply_keyboard = [['Пропустить']]
    update.message.reply_text('Отправьте краткое видео о себе, либо кнопку "Пропустить" для пропуска шага',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return 7


def video(update, context):
    user = str(update.message.from_user['username'])
    video_file = update.message.video.get_file()
    video_file.download(user + 'video.mp4')
    update.message.reply_text('Мы с вами свяжемся.')
    return ConversationHandler.END


def skip_photo(update, context):
    reply_keyboard = [['Пропустить']]
    update.message.reply_text('Отправьте свое резюме, либо кнопку "Пропустить" для пропуска шага',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return 6


def skip_bio(update, context):
    reply_keyboard = [['Пропустить']]
    update.message.reply_text('Отправьте краткое видео о себе, либо кнопку "Пропустить" для пропуска шага',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return 7


def skip_video(update, context):
    update.message.reply_text('Мы с вами свяжемся.')
    return ConversationHandler.END


def phonebook(update, context):
    print(update.message.text)
    reply_keyboard = [['Записать номер', 'Найти номер', 'Найти имя']]
    update.message.reply_text('Выберите функцию: ',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return 1


def write(update, context):
    update.message.reply_text('Введите Номер, а затем Имя через Пробел: ')
    return 2


def write_do(update, context):
    answer = update.message.text
    context.bot.send_message(update.effective_chat.id, write_down(answer.split()[0], answer.split()[1]))
    return ConversationHandler.END


def find_number(update, context):
    update.message.reply_text('Введите Имя или Номер для поиска: ')
    return 3


def find_number_do(update, context):
    context.bot.send_message(update.effective_chat.id, find(update.message.text))
    return ConversationHandler.END


def cancel(update):
    update.message.reply_text('Пишите еще.')
    return ConversationHandler.END
