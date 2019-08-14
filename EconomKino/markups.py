from telebot import types
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

import datetime
from datetime import datetime as dt
from babel.dates import format_datetime

from EconomKino import const

# MAIN MENU REPLY MARKUP
main_menu = types.ReplyKeyboardMarkup(True, False)
main_menu.row(const.CINEMA_EMOJI + ' Старт', const.LOCATION_EMOJI + ' Локації', const.INFO_EMOJI + ' Інфо')


# CINEMAS REPLY MARKUP
cinemas_markup = types.ReplyKeyboardMarkup(True, False)
cinemas_markup.row('Планета Кіно: Forum ' + const.NIGHT_CITY_EMOJI, 'Multiplex:\nSpartak ' + const.RUNNER_EMOJI)
cinemas_markup.row('Планета Кіно:\nKing Cross ' + const.CROWN_EMOJI, 'Multiplex:\nVictoria Gardens ' + const.TREE_EMOJI)
cinemas_markup.row(const.LEFTWARDS_ARROW_EMOJI + ' Назад')


# CALENDAR INLINE MARKUP
# day_01 is today, day_02 - tomorrow and so on
day_01 = dt.today()
day_02 = dt.today() + datetime.timedelta(1)
day_03 = dt.today() + datetime.timedelta(2)
day_04 = dt.today() + datetime.timedelta(3)
day_05 = dt.today() + datetime.timedelta(4)
day_06 = dt.today() + datetime.timedelta(5)

day_01_locale = format_datetime(day_01, 'EE: dd.MM', locale='uk_UA')
day_02_locale = format_datetime(day_02, 'EE: dd.MM', locale='uk_UA')
day_03_locale = format_datetime(day_03, 'EE: dd.MM', locale='uk_UA')
day_04_locale = format_datetime(day_04, 'EE: dd.MM', locale='uk_UA')
day_05_locale = format_datetime(day_05, 'EE: dd.MM', locale='uk_UA')
day_06_locale = format_datetime(day_06, 'EE: dd.MM', locale='uk_UA')

day_01_callback = format_datetime(day_01, 'dd_MM')
day_02_callback = format_datetime(day_02, 'dd_MM')
day_03_callback = format_datetime(day_03, 'dd_MM')
day_04_callback = format_datetime(day_04, 'dd_MM')
day_05_callback = format_datetime(day_05, 'dd_MM')
day_06_callback = format_datetime(day_06, 'dd_MM')

calendar_markup = InlineKeyboardMarkup()
calendar_markup.add(InlineKeyboardButton(text=day_01_locale, callback_data=day_01_callback),
                    InlineKeyboardButton(text=day_02_locale, callback_data=day_02_callback),
                    InlineKeyboardButton(text=day_03_locale, callback_data=day_03_callback),
                    InlineKeyboardButton(text=day_04_locale, callback_data=day_04_callback),
                    InlineKeyboardButton(text=day_05_locale, callback_data=day_05_callback),
                    InlineKeyboardButton(text=day_06_locale, callback_data=day_06_callback))