from EconomKino import token, const, markups, logger, threads, parsers

import telebot
from telebot.types import Message


threads.SessionsRefresher().start()

bot = telebot.TeleBot(token.TOKEN)


# PROCESSING COMMANDS
@bot.message_handler(commands=['start'])
def message_handler(message: Message):
    bot.send_message(message.from_user.id,
                     text=('Привіт!\nЯ Економ Кіно Бот ' + const.POPCORN_EMOJI),
                     reply_markup=markups.main_menu)
    logger.log_message(message)


@bot.message_handler(commands=['help'])
def message_handler(message: Message):
    bot.send_message(message.from_user.id, const.INFO, reply_markup=markups.main_menu)
    logger.log_message(message)


# PROCESSING REPLY KEYBOARD
@bot.message_handler(content_types='text')
def text_handler(message: Message):
    if message.text == const.LEFTWARDS_ARROW_EMOJI + ' Назад':
        bot.send_message(message.from_user.id, '...', reply_markup=markups.main_menu)

    # Main menu
    elif message.text == const.CINEMA_EMOJI + ' Старт':
        bot.send_message(message.from_user.id, 'Виберіть день:', reply_markup=markups.calendar_markup)
    elif message.text == const.LOCATION_EMOJI + ' Локації':
        bot.send_message(message.from_user.id, 'Виберіть кінотеатр:', reply_markup=markups.cinemas_markup)
    elif message.text == const.INFO_EMOJI + ' Інфо':
        bot.send_message(message.from_user.id, const.INFO)

    # Cinemas location
    elif message.text == 'Multiplex:\nVictoria Gardens ' + const.TREE_EMOJI:
        bot.send_message(message.from_user.id, 'Шукаю Локацію ' + const.SEARCH_EMOJI)
        bot.send_location(message.from_user.id, 49.807352, 23.977764)
    elif message.text == 'Планета Кіно: Forum ' + const.NIGHT_CITY_EMOJI:
        bot.send_message(message.from_user.id, 'Шукаю Локацію ' + const.SEARCH_EMOJI)
        bot.send_location(message.from_user.id, 49.849907, 24.022289)
    elif message.text == 'Планета Кіно:\nKing Cross ' + const.CROWN_EMOJI:
        bot.send_message(message.from_user.id, 'Шукаю Локацію ' + const.SEARCH_EMOJI)
        bot.send_location(message.from_user.id, 49.7734383, 24.0113537)
    elif message.text == 'Multiplex:\nSpartak ' + const.RUNNER_EMOJI:
        bot.send_message(message.from_user.id, 'Шукаю Локацію ' + const.SEARCH_EMOJI)
        bot.send_location(message.from_user.id, 49.869722, 24.0223554)
    logger.log_message(message)


print('It\'s working...')
bot.polling(none_stop=True)
