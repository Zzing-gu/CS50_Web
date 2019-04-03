import os
import requests

from flask import Flask, jsonify, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

channels = {"yes": [], "no": [], "maybe": []}


@app.route("/")
def index():
    return render_template("index.html", channels=channels)


def error(message):
    return  message   


@app.route("/create/<string:chname>")
def create(chname):
    
    if chname in channels:
        error('already exist channel name!')
        return jsonify({"error ": "channel name already exist"}), 404
    else:
        channels[chname] = []
        print(channels)
    return index()



@socketio.on("send text")
def text(data):
    text = data["text"]
    emit("announce text", {"text": text}, broadcast=True)