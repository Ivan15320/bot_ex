from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from telebot import TeleBot

def gen_start_markup():
    # Создаём объекты кнопок.
    button_1 = KeyboardButton(text="Выбрать лекарcтво")

    # Создаём объект клавиатуры, добавляя в него кнопки.
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(button_1)
    return keyboard