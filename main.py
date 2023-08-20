import telebot
import buttons
from telebot import types
from telebot.types import ReplyKeyboardRemove
import db

bot = telebot.TeleBot('5871610659:AAGx34S-Q7zdiLtqGYoWH2uHdysUigV4Lig')

genre_list = ['Полиция', 'Сверхъестественное', 'Экшен', 'Демоны', 'Исторический', 'Психологическое', 'Игры', 'Супер сила', 'Комедия', 'Фантастика', 'Фентези', 'Приключение', 'Драма', 'Триллер', 'Сёнэн', 'Ужасы', 'Детектив', 'Романтика']

@bot.message_handler(commands=['start'])
def start_message(message):
    user_id = message.from_user.id

    bot.send_message(user_id, 'Как хотите найти аниме?', reply_markup=buttons.buttons1())



@bot.message_handler(content_types=['text'])
def function(message):
    user_id =message.from_user.id
    user_name = message.chat.first_name

    if message.text == 'Искать по жанрам':
        bot.send_message(user_id, user_name, reply_markup=types.ReplyKeyboardRemove())
        bot.send_message(user_id, 'Выберите жанр:', reply_markup=buttons.genres_kb())

        bot.register_next_step_handler(message, genre_func)

    else:
        bot.send_message(user_id, 'Нажмите кнопку!')

def genre_func(message):

    user_id = message.from_user.id
    user_name = message.chat.first_name

    genre = message.text
    if genre in genre_list:

        db.adding_genre_to_user_genre_list(user_id, genre)

        bot.send_message(user_id, 'Выберите ещё жанр?')
        bot.register_next_step_handler(message, genre_func)

    elif genre == 'Искать!':
        a = db.get_genre(user_id)
        bot.send_message(user_id, user_name, reply_markup=ReplyKeyboardRemove())
        bot.send_message(user_id, a, reply_markup=buttons.buttons1())
        db.clearing_user_genre_list(user_id, )





bot.polling(none_stop=True)