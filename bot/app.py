import os
from flask import Flask, request
import telebot
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
URL = os.getenv('URL')
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Привет {message.chat.first_name}!')


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.send_message(message.chat.id, message.text)


@app.route(f'/{TOKEN}/', methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


@app.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=URL)
    return "!", 200


if __name__ == "__main__":
    app.run()
