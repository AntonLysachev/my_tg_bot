import telebot
import os
from dotenv import load_dotenv


load_dotenv()
token = os.getenv('TOKEN')

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет!')

bot.polling(none_stop=True)