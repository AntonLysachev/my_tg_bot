import requests
import os
from dotenv import load_dotenv
from flask import Flask, request


load_dotenv()
token = os.getenv('TOKEN')
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


def send_message(chat_id, text, token):
    method = 'sendMessage'
    url = f'https://api.telegram.org/bot{token}/{method}'
    data = {'chat_id': chat_id, 'text': text}
    requests.post(url, data=data)

@app.route('/', methods=['POST'])
def process():
    data = request.json
    if data.get('message', False):
        chat_id = request.json['message']['chat']['id']
        name = request.json['message']['from']['first_name']
    else:
        chat_id = request.json['edited_message']['chat']['id']
        name = request.json['edited_message']['from']['first_name']
    send_message(chat_id, f'Привет {name}!', token)
    return {'ok': True}

debug_switch = os.getenv('DEBUG_SWITCH')

if __name__ == '__main__':
    app.run(debug=debug_switch)
