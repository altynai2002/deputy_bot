import os
from telebot import TeleBot
import config
import search

bot = TeleBot(config.TOKEN)

# Вызывается клавиатура с приветствием
@bot.message_handler(commands=['start','help'])
def send_hello(message):
    bot.reply_to(message, 'Здравствуйте, введите фамилию депутата.')

# Выводит информацию о депутате
@bot.message_handler(func=lambda m: True)
def send_info(message):
    name = message.text
    deputy = search.get_info(name)
    bot.reply_to(message, f'{deputy}\n')




if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)

