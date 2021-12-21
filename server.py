from flask import Flask, request, render_template
import time
from datetime import datetime

app = Flask(__name__)


def time_format(t):
    return datetime.fromtimestamp(t)


all_messages = [  # В этом списке хранятся все сообщения чата
    {  # каждое сообщение это словарь с полями text, name и time
        "text": 'Привет всем в чате',
        "name": "Mike",
        "time": time_format(time.time() - 3600)  # типа майк написал сообщение час (3600 сек) назад
    },
]


@app.route("/chat")
def chat():
    return render_template("chat.html")


@app.route("/get_messages")  # GET — запрос на чтение данных
def get_messages():
    return {"messages": all_messages}


@app.route("/")
def root():
    return "Hello everyone"


# POST — запрос на изменение данных

@app.route("/send")
def send_message():
    # ToDO Проверить text и name

    text = request.args["text"]
    name = request.args["name"]

    # Проверить что имя не очень длинное
    if (len(name) < 3) or (len(name) > 100):
        return "ERROR NAME" # куда пишет сообщение? В какую консоль?

    # ToDo: сделать еще проверки

    # Проверка длины текстового сообщения
    if (len(text) < 1) or (len(text) > 3000):
        return "ERROR TEXT" # куда пишет сообщение? В какую консоль?


    message = {
        "text": text,
        "name": name,
        "time": time_format(time.time()),
    }

    all_messages.append(message)

    return "OK" # И это куда пишет?


app.run()