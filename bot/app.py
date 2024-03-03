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
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)


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




# import os
# from dotenv import load_dotenv
# from flask import Flask, request, abort
# import telebot
# import logging
# import json


# load_dotenv()
# TOKEN = os.getenv('TOKEN')
# URL = os.getenv('URL')
# logger = telebot.logger
# telebot.logger.setLevel(logging.INFO)
# bot = telebot.TeleBot(TOKEN)


# app = Flask(__name__)
# app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


# @app.route('/', methods=['GET', 'HEAD'])
# def index():
#     return ''


# @app.route(f'/{TOKEN}/', methods=['POST'])
# def webhook():
#     if request.headers.get('content-type') == 'application/json':
#         json_string = request.get_data().decode('utf-8')
#         update = telebot.types.Update.de_json(json_string)
#         bot.process_new_updates([update])
#         return ''
#     else:
#         abort(403)


# @bot.message_handler(commands=['help', 'start'])
# def send_welcome(message):
#     bot.send_message(message.chat.id, f'Привет {message.chat.first_name}!')


# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     bot.send_message(message.chat.id, f'Привет {message.chat.first_name}!')


# bot.remove_webhook()
# bot.set_webhook(url=URL)

# debug_switch = os.getenv('DEBUG_SWITCH')

# if __name__ == '__main__':
#     app.run(debug=debug_switch)
