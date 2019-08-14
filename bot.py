from EconomKino import token, const, markups

import telebot
from telebot.types import Message

bot = telebot.TeleBot(token.TOKEN)
print("It's working...")


@bot.message_handler(commands=['start'])
def message_handler(message: Message):
    bot.send_message(message.from_user.id,
                     text=('Привіт!\nЯ Економ Кіно Бот ' + const.POPCORN_EMOJI),
                     reply_markup=markups.main_menu)


bot.polling(none_stop=True)
