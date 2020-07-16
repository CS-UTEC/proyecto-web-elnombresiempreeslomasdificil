#!/usr/bin/env python3

from flask import Flask, render_template, request, session, Response, redirect
from xdg import BaseDirectory
from os import path

import json
import time
import threading

if __package__ is None or __package__ == '':
    from database import connector
    from model import entities
else:
    from .database import connector
    from .model import entities

db = connector.Manager()
engine = db.createEngine()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def getIndex():
    return render_template('index.html')


@app.route('/static/<content>')
def static_content(content):
    print(content)
    return render_template(content)


def main():
    print(BaseDirectory.xdg_data_home)
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))


if __name__ == '__main__':
    main()
