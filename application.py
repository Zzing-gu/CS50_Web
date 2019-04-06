import os
import requests

from flask import Flask, jsonify, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

channels = {"yes": [1,8782,3], "no": [1,2,6783], "maybe": [5675671,2,3]}


@app.route("/")
def index():
    return render_template("index.html", channels=channels)


def error(message):
    return  message   

@app.route("/select/<string:channel>")
def select(channel):
    selected = channel
    return render_template("index.html", channels=channels , selected=channels[selected])

@app.route("/create" , methods=["POST"])
def create():
    chname = request.form.get("channelname")
    if chname in channels:
        
        return jsonify({"error ": "channel name already exist"}), 404
    else:
        channels[chname] = []
        print(channels)
    return index()



@socketio.on("send text")
def text(data):
    text = data["text"]
    chname = data["chname"]
    print(channels)
    if len(channels[chname])> 100:
        channels[chname].pop(0)
        channels[chname].append(text)
    else:
        channels[chname].append(text)
    
    emit("announce text", {"text": text}, broadcast=True)



# @socketio.on("back to channel")
# def back(data):
   
#     print('welcome back')
#     print(selected)
#     return render_template("index.html", channels=channels , selected=channels[data])