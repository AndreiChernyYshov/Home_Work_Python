from telegram.ext import ConversationHandler
from telegram import ReplyKeyboardMarkup
from data import *

START_CHOICE = 0
SUMMARY = 1
PHONEBOOK = 1
PHONEBOOK_CHOICE = 2
WRITE = 3
WRITE_DO = 4
FIND_NUMBER = 3
FIND_NUMBER_DO = 4
FIND_NAME = 3


def start(update, context):
    reply_keyboard = [['Телефонный справочник', 'Заполнить резюме']]
    update.message.reply_text('Выберите функцию: ',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return START_CHOICE


def start_choice(update, context):
    if update.message.text == 'Телефонный справочник':
        return PHONEBOOK
    elif update.message.text == 'Заполнить резюме':
        return SUMMARY


def summary(update, context):
    print('cвч')
    return ConversationHandler.END


def phonebook(update, context):
    print(update.message.text)
    reply_keyboard = [['Записать номер', 'Найти номер', 'Найти имя']]
    update.message.reply_text('Выберите функцию: ',
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return PHONEBOOK_CHOICE


def phonebook_choice(update, context):
    if update.message.text == 'Записать номер':
        return WRITE
    if update.message.text == 'Найти номер':
        return FIND_NUMBER
    elif update.message.text == 'Найти имя':
        update.message.reply_text('Введите Имя: ')
        return FIND_NAME


def write(update, context):
    update.message.reply_text('Введите Номер, а затем Имя через Пробел: ')
    return WRITE_DO


def write_do(update, context):
    answer = update.message.text
    context.bot.send_message(update.effective_chat.id, write_down(answer.split()[0], answer.split()[1]))
    return ConversationHandler.END


def find_number(update, context):
    update.message.reply_text('Введите Имя: ')
    return FIND_NUMBER_DO


def find_number_do(update, context):
    context.bot.send_message(update.effective_chat.id, find(update.message.text))
    return ConversationHandler.END


def cancel(update):
    update.message.reply_text('Пишите еще.')
    return ConversationHandler.END
