import sqlite3

connection = sqlite3.connect('database.db')

sql = connection.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS user_genre_list(tg_id INTEGER, user_genres TEXT);')

def adding_genre_to_user_genre_list(tg_id, user_genres):

    connection = sqlite3.connect('database.db')
    sql = connection.cursor()

    sql.execute('INSERT INTO user_genre_list (tg_id, user_genres) VALUES (?, ?)', (tg_id, user_genres))

    connection.commit()

def clearing_user_genre_list(tg_id):

    connection = sqlite3.connect('database.db')
    sql = connection.cursor()

    sql.execute('DELETE FROM user_genre_list WHERE tg_id=?;', (tg_id, ))

    connection.commit()

def get_genre(tg_id):

    connection = sqlite3.connect('database.db')
    sql = connection.cursor()

    a = sql.execute('SELECT user_genres FROM user_genre_list WHERE tg_id=?', (tg_id, ))
    sorted_a = [i for i in a]

    return sorted_a