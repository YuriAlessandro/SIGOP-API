# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
from functions.users import *
from functions.offers import *
from functions.favorites import *

from models.user import User
from models.offer import Offer
from models.favorite import Favorite
from models.avaliation import Avaliation

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
    

@app.route('/auth/sigaa', methods=['POST'])
def auth_user_sigaa():
    """
    """
    params = request.args
    
    email = params.get('email')
    username = params.get('username')
    
    user_id = params.get('user_id')
    first_name = params.get('first_name')
    last_name = params.get('last_name')
    status = params.get('status')
    password = params.get('password')
    user_type = params.get('type')
    unity = params.get('unity')
    
    user = User(0, first_name, last_name,
                status, username, email, password,
                user_type, unity)
    
    return jsonify(auth_sigaa(email, username, user))

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

        offer = Offer(offer_id, title, description, user_id,
                end_offer, email, phone, offer_type, salary_aids,
                salary_total, location, latitude, longitude)

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

@app.route('/offers/<int:offer_id>/avaliations', methods=['GET', 'POST'])
def avaliation(offer_id):
    
    params = request.args

    if request.method == 'GET':
        return jsonify(list_avaliations(offer_id))
    
    elif request.method == 'POST':
        user_id = params.get('logged_user_id')
        if not user_id:
            return jsonify({'success':False, 'msg': 'missing logged_user_id'})
        
        avaliation_id = params.get('avaliation_id')
        date = params.get('date')
        value = params.get('value')
        text = params.get('text')
    
        avaliation = Avaliation(avaliation_id, date, offer_id,
                                user_id, value, text)
        return jsonify(insert_avaliation(avaliation))
    return jsonify({'success': True})


@app.route('/favorites', methods=['GET', 'POST'])
def favorite():
    """ Favorite """
    params = request.args
    user_id = params.get('logged_user_id')

    if not user_id:
        return jsonify({'success':False, 'msg': 'missing logged_user_id'})

    if request.method == 'GET':
        return jsonify(list_favorites(user_id))

    elif request.method == 'POST':
        offer_id = params.get('offer_id')

        favorite = Favorite(user_id, offer_id)

        return jsonify(insert_favorite(favorite))

    return jsonify({'success': True})


@app.route('/myOffers/<int:user_id>', methods=['GET'])
def useroffer(user_id):
    
    params = request.args
    
    if not user_id:
            return jsonify({'success':False, 'msg': 'missing logged_user_id'})
    
    return jsonify(list_offers_by_id(user_id))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
