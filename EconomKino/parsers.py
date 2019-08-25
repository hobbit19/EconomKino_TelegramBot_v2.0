import requests
from bs4 import BeautifulSoup as bs
from babel.dates import format_datetime

from EconomKino import markups
from EconomKino.const import OK


# day_01 is today, day_02 - tomorrow and so on
# Lists with all sessions in chosen date
day_01_sessions = []
day_02_sessions = []
day_03_sessions = []
day_04_sessions = []
day_05_sessions = []
day_06_sessions = []

# Lists with available films in chosen date
day_01_films = set()
day_02_films = set()
day_03_films = set()
day_04_films = set()
day_05_films = set()
day_06_films = set()

viktoria_url = 'https://multiplex.ua/ua/cinema/lviv/victoriagardens'
spartak_url = 'https://multiplex.ua/ua/cinema/lviv/spartak'


def get_technology(arg):
    if '3D' in arg:
        return '3D'
    elif len(arg) == 0 or (arg == 'LUX '):
        return '2D'
    else:
        return '2D'


def parse_multiplex(base_url, date, cinema):
    films = []
    session = requests.Session()
    request = session.get(base_url)

    if request.status_code == OK:
        soup = bs(request.content, 'html.parser')
        sessions = soup.find_all('div', attrs={'data-anchor': date})
        for tag in sessions:
            films.append({'film-name': tag.attrs['data-name'],
                          'price': tag.attrs['data-low'][0: len(tag.attrs['data-low'])-2],
                          'time': tag.find('span').text,
                          'technology': get_technology(tag.find('p', class_='tag').text),
                          'cinema-id': cinema,
                          'tickets_url': base_url})
    else:
        print("ERROR Bad request")
    return films


def parse_all():
    global day_01_sessions, day_02_sessions, day_03_sessions, day_04_sessions, day_05_sessions, day_06_sessions

    day_01_sessions += parse_multiplex(viktoria_url, format_datetime(markups.day_01, 'ddMMYYYY', locale='uk_UA'), 2)
    day_02_sessions += parse_multiplex(viktoria_url, format_datetime(markups.day_02, 'ddMMYYYY', locale='uk_UA'), 2)
    day_03_sessions += parse_multiplex(viktoria_url, format_datetime(markups.day_03, 'ddMMYYYY', locale='uk_UA'), 2)
    day_04_sessions += parse_multiplex(viktoria_url, format_datetime(markups.day_04, 'ddMMYYYY', locale='uk_UA'), 2)
    day_05_sessions += parse_multiplex(viktoria_url, format_datetime(markups.day_05, 'ddMMYYYY', locale='uk_UA'), 2)
    day_06_sessions += parse_multiplex(viktoria_url, format_datetime(markups.day_06, 'ddMMYYYY', locale='uk_UA'), 2)

    day_01_sessions += parse_multiplex(spartak_url, format_datetime(markups.day_01, 'ddMMYYYY', locale='uk_UA'), 1)
    day_02_sessions += parse_multiplex(spartak_url, format_datetime(markups.day_02, 'ddMMYYYY', locale='uk_UA'), 1)
    day_03_sessions += parse_multiplex(spartak_url, format_datetime(markups.day_03, 'ddMMYYYY', locale='uk_UA'), 1)
    day_04_sessions += parse_multiplex(spartak_url, format_datetime(markups.day_04, 'ddMMYYYY', locale='uk_UA'), 1)
    day_05_sessions += parse_multiplex(spartak_url, format_datetime(markups.day_05, 'ddMMYYYY', locale='uk_UA'), 1)
    day_06_sessions += parse_multiplex(spartak_url, format_datetime(markups.day_06, 'ddMMYYYY', locale='uk_UA'), 1)


def create_film_lists():
    for session in day_01_sessions:
        day_01_films.add(session['film-name'])
    for session in day_02_sessions:
        day_02_films.add(session['film-name'])
    for session in day_03_sessions:
        day_03_films.add(session['film-name'])
    for session in day_04_sessions:
        day_04_films.add(session['film-name'])
    for session in day_05_sessions:
        day_05_films.add(session['film-name'])
    for session in day_06_sessions:
        day_06_films.add(session['film-name'])
