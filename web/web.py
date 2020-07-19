#!/usr/bin/env python3

from flask import Flask, render_template, request, Response, session
from xdg import BaseDirectory
from os import path

import json

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


@app.route('/users', methods=['POST'])
def create_user():
    # c = json.loads(request.data)
    if(not request.is_json):
        c = json.loads(request.form['values'])
    else:
        c = json.loads(request.data)

    user = entities.User(
        username=c['username'],
        password=c['password']
    )
    _session = db.getSession(engine)
    _session.add(user)
    _session.commit()
    _session.close()
    r_msg = {'msg': 'UserCreated'}
    return Response(json.dumps(r_msg), status=201)


@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    db_session = db.getSession(engine)

    if(id == "-1"):
        id = session['id']

    users = db_session.query(entities.User).filter(entities.User.id == id)
    db_session.close()
    for user in users:
        js = json.dumps(user, cls=connector.AlchemyEncoder)
        return Response(js, status=200, mimetype='application/json')
    message = {'status': 404, 'message': 'Not Found'}
    return Response(json.dumps(message),
                    status=404,
                    mimetype='application/json')


@app.route('/users', methods=['GET'])
def get_users():
    db_session = db.getSession(engine)

    users = db_session.query(entities.User)
    db_session.close()
    response = json.dumps(users[:], cls=connector.AlchemyEncoder)

    return Response(response, mimetype='application/json')


@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    _session = db.getSession(engine)
    user = _session.query(entities.User).filter(entities.User.id == id).first()
    c = json.loads(request.form['values'])

    for key in c.keys():
        setattr(user, key, c[key])

    _session.add(user)
    _session.commit()
    _session.close()

    message = {'message': 'Ok'}
    return Response(json.dumps(message), mimetype='application/json')


@app.route('/users/<id>', methods=['DELETE'])
def delete_user():
    _session = db.getSession(engine)
    user = _session.query(entities.User).filter(entities.User.id == id).one()
    _session.delete(user)
    _session.commit()
    _session.close()

    message = {'message': 'Ok'}
    return Response(json.dumps(message), mimetype='application/json')


def main():
    print(path.join(BaseDirectory.xdg_data_home, "web"))
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))


if __name__ == '__main__':
    main()
