import transliterate as transliterate
import re


def is_english(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True


def to_callback_data(name):
    res = re.sub("[,.:;!?\-]", "", name)
    if is_english(res):
        return re.sub(" ", "_", res)
    else:
        return transliterate.translit(res, reversed=True).replace(' ', '_')
