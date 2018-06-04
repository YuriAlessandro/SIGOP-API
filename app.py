# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
from functions.users import *

from models.user import User

app = Flask(__name__)

@app.route('/')
def main():
    """
        Main route
    """
    return ""

@app.route('/auth', methods=['POST'])
def login():
    """ Verify logged user
    """
    params = request.form

    username = params.get('username')
    password = params.get('password')

    return jsonify(auth(username, password))

@app.route('/users', methods=['GET', 'POST'])
def users():
    """
        Handle users endpoint
    """
    params = request.args

    if request.method == 'GET':
        # Listar todos os usuários
        return jsonify(list_users())

    elif request.method == 'POST':
        # Inserir um usuário
        user_id = params.get('user_id')
        first_name = params.get('first_name')
        last_name = params.get('last_name')
        status = params.get('status')
        login = params.get('username')
        email = params.get('email')
        password = params.get('password')
        user_type = params.get('type')
        unity = params.get('unity')

        user = User(user_id, first_name, last_name,
                    status, login, email, password,
                    user_type, unity)
        return jsonify(insert_user(user))

    return jsonify({'success': False})

@app.route('/users/<int:user_id>', methods=['GET', 'PATCH', 'DELETE'])
def user(user_id):

    if request.method == 'GET':
        return jsonify(get_user(user_id))
    elif request.method == 'PATCH':
        return jsonify({'success': False, 'error': 'Not implemented yet'})
    elif request.method == 'DELETE':
        return jsonify({'success': False, 'error': 'Not implemented yet'})
    
    return jsonify({'success': False})
    