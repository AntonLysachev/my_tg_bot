import os
from flask import Flask, request
import telebot
from dotenv import load_dotenv
import logging

load_dotenv()

BOT_TOKEN = os.getenv('TOKEN')
APP_URL = os.getenv('URL')

bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Привет {message.chat.first_name}!')


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.send_message(message.chat.id, message.text)


@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)    
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
