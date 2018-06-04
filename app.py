# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
import functions

from models.user import User

app = Flask(__name__)

@app.route('/')
def main():
    """
        Main route
    """
    return ""

@app.route('/users', methods=['GET', 'POST'])
def users():
    """
        Handle users endpoint
    """
    params = request.args

    if request.method == 'GET':
        # Listar todos os usuários
        return jsonify(functions.list_users())

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
        return jsonify(functions.insert_user(user))
