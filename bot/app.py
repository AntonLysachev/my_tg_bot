import os
from dotenv import load_dotenv
from flask import Flask, request, abort
import telebot
import logging


load_dotenv()
TOKEN = os.getenv('TOKEN')
URL = os.getenv('URL')
logger = telebot.logger
telebot.logger.setLevel(logging.INFO)
bot = telebot.TeleBot(TOKEN)


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route('/', methods=['GET', 'HEAD'])
def index():
    return ''


@app.route(f'/{TOKEN}/', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return 'ok'
    else:
        abort(403)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    print(message)
    bot.send_message(message.chat.id, f'Привет {message.chat.first_name}!')


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, f'Привет {message.chat.first_name}!')


bot.remove_webhook()
bot.set_webhook(url=URL)

debug_switch = os.getenv('DEBUG_SWITCH')

if __name__ == '__main__':
    app.run(debug=debug_switch)
