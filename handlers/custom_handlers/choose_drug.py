from telebot.types import Message
from loader import bot
import database
import sqlite3



@bot.message_handler(func=lambda message: message.text == "Выбрать лекарcтво")
def choose_disease(message: Message):
    in_message = bot.send_message(
        message.chat.id, f"Введите название лекарcтва"
    )
    bot.register_next_step_handler(in_message, callback=city)


def city(message):
    database.database.exist()
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()
    # Добавляем нового пользователя
    cursor.execute('INSERT INTO Users (id, username, medicine) VALUES (?, ?, ?)', (message.chat.id, message.from_user.username, message.text))

    # Сохраняем изменения и закрываем соединение
    connection.commit()
    cursor.execute('SELECT * FROM Users')
    users = cursor.fetchall()
    connection.close()

    bot.send_message(
        message.chat.id, f": {users}"
    )
city("23")