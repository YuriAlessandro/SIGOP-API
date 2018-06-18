# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
from functions.users import *
from functions.offers import *

from models.user import User
from models.offer import Offer

app = Flask(__name__)

@app.route('/')
def main():
    """
        Main route
    """
    return ""

@app.route('/auth', methods=['POST'])
def auth_user():
    """ Verify logged user
    """
    params = request.args

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

@app.route('/offers', methods=['GET', 'POST'])
def offers():
    """ Offers """

    params = request.args
    
    user_id = params.get('logged_user_id')
    if not user_id:
            return jsonify({'success':False, 'msg': 'missing logged_user_id'})
    
    if request.method == 'GET':
        return jsonify(list_offers(user_id))


    elif request.method == 'POST':
        offer_id = params.get('offer_id')
        title = params.get('title')
        description = params.get('description')
        end_offer = params.get('endOffer')
        email = params.get('email')
        phone = params.get('phone')
        offer_type = params.get('offer_type')
        salary_aids = params.get('salary_aids')
        salary_total = params.get('salary_total')
        location = params.get('location')
        latitude = params.get('latitude')
        longitude = params.get('longitude')

        offer = Offer(offer_id, title, description, user_id, end_offer, email, phone)

        return jsonify(insert_offer(offer))

    return jsonify({'success': True})

@app.route('/offers/<int:offer_id>', methods=['GET', 'POST'])
def offer(offer_id):

    params = request.args

    if request.method == 'GET':
        user_id = params.get('logged_user_id')
        if not user_id:
            return jsonify({'success':False, 'msg': 'missing logged_user_id'})
        return jsonify(get_offer(offer_id, user_id)) 
        
    elif request.method == 'POST':
        # YURI UM DIA VAI FAZER
        pass

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
