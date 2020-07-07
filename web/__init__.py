#!/usr/bin/env python3

from flask import Flask,render_template, request, session, Response, redirect
from database import connector
from model import entities
import json
import time
import threading

db = connector.Manager()
engine = db.createEngine()
app = Flask(__name__)


@app.route('/static/<content>')
def static_content(content):
    print(content)
    return render_template(content)


@app.route('/', methods=['GET'])
def getIndex():
    return render_template('index.html')


if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))

