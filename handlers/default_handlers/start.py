from telebot.types import Message
from keyboards.reply import start_keyboard
from loader import bot


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    bot.reply_to(message,
                 f"Привет, {message.from_user.full_name}! Я бот помошник по лекарствам. Подскажу когда что принимать.",
                 reply_markup=start_keyboard.gen_start_markup())

