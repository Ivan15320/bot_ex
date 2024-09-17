import sqlite3


def exist():
    # Устанавливаем соединение с базой данных
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()

    # Создаем таблицу Users
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users_history (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    medicine TEXT NOT NULL
    )
    ''')

    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()

