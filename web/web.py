#!/usr/bin/env python3

from markdown import markdown
from flask import Flask, render_template, request, Response, session
from os import path
from pathlib import Path

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


@app.route('/authenticate', methods=['POST'])
def authenticate() -> str:
    body = json.loads(request.data)
    username: str = body['username']
    password: str = body['password']

    db_session = db.getSession(engine)
    users = db_session.query(entities.User).\
        filter(entities.User.username == username)

    db_session.close()
    for i in users:
        if (i.password == password):
            # with app.app_context():
            # user_id = i.id
            session['id'] = i.id

            response = {'msg': 'ok', 'id': i.id, 'username': username}
            return Response(json.dumps(response), mimetype='application/json')

    return Response('{"msg": "No"}', status=401, mimetype='application/json')


@app.route('/', methods=['GET'])
def getIndex():
    return render_template('index.html')


@app.route('/static/<content>')
def static_content(content):
    print(content)
    return render_template(content)


@app.route('/users', methods=['POST'])
def create_user():
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


@app.route('/markdown')
def markdown_test():
    print("markdown")
    return markdown('# Hello world')


@app.route('/recipes2', methods=['POST'])
def create_recipe2():
    if(not request.is_json):
        c = json.loads(request.form['values'])
    else:
        c = json.loads(request.data)

    recipe = entities.Recipe2(
        user_id=c['user_id'],
        md_file='.md',
        json_file='.json'
    )

    _session = db.getSession(engine)
    _session.add(recipe)
    _session.commit()

    recipe.md_file = str(recipe.id) + recipe.md_file
    recipe.json_file = str(recipe.id) + recipe.json_file

    Path(entities.recipe_data_dir).mkdir(parents=True, exist_ok=True)

    markdown_path = path.join(entities.recipe_data_dir, recipe.md_file)
    json_path = path.join(entities.recipe_data_dir, recipe.json_file)

    markdown_file = open(markdown_path, 'w')
    json_file = open(json_path, 'w')

    markdown_file.write(c['markdown'])
    json_file.write(json.dumps({'tags': c['tags']}))

    markdown_file.close()
    json_file.close()

    _session.close()

    r_msg = {'msg': 'Recipe created'}
    return Response(json.dumps(r_msg), status=201)


@app.route('/recipes2', methods=['GET'])
def get_recipes2():
    user = int(request.args.get('user'))

    db_session = db.getSession(engine)

    recipes = db_session.query(entities.Recipe2)

    if user is not None:
        recipes = recipes.filter(entities.Recipe2.user_id == user)

    db_session.close()
    response = json.dumps([x.to_json_dict() for x in recipes[:]])

    return Response(response, mimetype='application/json')


def main():
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))


if __name__ == '__main__':
    main()
