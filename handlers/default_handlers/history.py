from telebot.types import Message



from loader import bot


@bot.message_handler(commands=["history"])
def bot_help(message: Message):
    text = ''
    bot.reply_to(message, "\n".join(text))