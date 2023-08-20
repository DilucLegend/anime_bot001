from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def buttons1():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    genres = KeyboardButton('Искать по жанрам')

    kb.add(genres)

    return kb


def genres_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)

    romantic = KeyboardButton(text='Романтика')
    detective = KeyboardButton(text='Детектив')
    horror = KeyboardButton(text='Ужасы')
    shonen = KeyboardButton(text='Сёнэн')
    thriller = KeyboardButton(text='Триллер')
    dramma = KeyboardButton(text='Драма')
    advanture = KeyboardButton(text='Приключение')
    fentesy = KeyboardButton(text='Фентези')
    fantastic = KeyboardButton(text='Фантастика')
    comedy = KeyboardButton(text='Комедия')
    super_power = KeyboardButton(text='Супер сила')
    games = KeyboardButton(text='Игры')
    police = KeyboardButton(text='Полиция')
    psychological = KeyboardButton(text='Психологическое')
    supernature = KeyboardButton(text='Сверхъестественное')
    action = KeyboardButton(text='Экшен')
    demons = KeyboardButton(text='Демоны')
    historical = KeyboardButton(text='Исторический')

    search = KeyboardButton(text='Искать!')

    kb.row(search)
    kb.add(romantic, detective, horror, shonen, thriller, dramma, advanture, fentesy, fantastic, comedy, super_power,
           games, police, psychological, supernature, action, demons, historical)

    return kb