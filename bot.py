import pymysql
import telebot
from telebot.types import Message
from babel.dates import format_datetime

from EconomKino import token, const, markups, logger, threads, parsers, functions


db = pymysql.connect(host="eu-cdbr-west-02.cleardb.net",
                     user="bdb28d30c292d7",
                     password="4ad2b3a3",
                     db="heroku_982b4fce6d3c135")
cursor = db.cursor()

users = []
new_users = []


sql_get_all_users = "SELECT * FROM heroku_982b4fce6d3c135.users;"
cursor.execute(sql_get_all_users)
get_all_users_result = cursor.fetchall()

for user in get_all_users_result:
    users.append({"user_id": user[0], "chosen_date": format_datetime(markups.day_01, "dd_MM")})


parsers.parse_all()
parsers.create_film_lists()
markups.update_film_lists_markup()

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


# PROCESSING INLINE KEYBOARD
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Dates
    if call.data == markups.day_01_callback:
        bot.edit_message_text(chat_id=call.from_user.id,
                              text="Фільми, які будуть в прокаті у цей день:",
                              message_id=call.message.message_id)
        bot.edit_message_reply_markup(chat_id=call.from_user.id,
                                      message_id=call.message.message_id,
                                      reply_markup=markups.day_01_films)
    elif call.data == markups.day_02_callback:
        bot.edit_message_text(chat_id=call.from_user.id,
                              text="Фільми, які будуть в прокаті у цей день:",
                              message_id=call.message.message_id)
        bot.edit_message_reply_markup(chat_id=call.from_user.id,
                                      message_id=call.message.message_id,
                                      reply_markup=markups.day_02_films)
    elif call.data == markups.day_03_callback:
        bot.edit_message_text(chat_id=call.from_user.id,
                              text="Фільми, які будуть в прокаті у цей день:",
                              message_id=call.message.message_id)
        bot.edit_message_reply_markup(chat_id=call.from_user.id,
                                      message_id=call.message.message_id,
                                      reply_markup=markups.day_03_films)
    elif call.data == markups.day_04_callback:
        bot.edit_message_text(chat_id=call.from_user.id,
                              text="Фільми, які будуть в прокаті у цей день:",
                              message_id=call.message.message_id)
        bot.edit_message_reply_markup(chat_id=call.from_user.id,
                                      message_id=call.message.message_id,
                                      reply_markup=markups.day_04_films)
    elif call.data == markups.day_05_callback:
        bot.edit_message_text(chat_id=call.from_user.id,
                              text="Фільми, які будуть в прокаті у цей день:",
                              message_id=call.message.message_id)
        bot.edit_message_reply_markup(chat_id=call.from_user.id,
                                      message_id=call.message.message_id,
                                      reply_markup=markups.day_05_films)
    elif call.data == markups.day_06_callback:
        bot.edit_message_text(chat_id=call.from_user.id,
                              text="Фільми, які будуть в прокаті у цей день:",
                              message_id=call.message.message_id)
        bot.edit_message_reply_markup(chat_id=call.from_user.id,
                                      message_id=call.message.message_id,
                                      reply_markup=markups.day_06_films)

    # Lists of films
    elif call.data == "back_to_calendar":
        bot.edit_message_text(chat_id=call.from_user.id,
                              text="Виберіть день: ",
                              message_id=call.message.message_id)
        bot.edit_message_reply_markup(chat_id=call.from_user.id,
                                      message_id=call.message.message_id,
                                      reply_markup=markups.calendar_markup)

    # Create
    elif call.data in parsers.day_01_films_callback:
        all_sessions = ""
        for ses in parsers.day_01_sessions:
            if functions.to_callback_data(ses.get("film-name")) == call.data:
                all_sessions += str(ses.get("price"))
                all_sessions += "\n"
        print(all_sessions)

    logger.log_call(call)


print('It\'s working...')
bot.polling(none_stop=True)
