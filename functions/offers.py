from functions.utils import connect_db


def list_offers(user_id):
    """ List all offers """
    cnx = connect_db()
    cur = cnx.cursor(buffered=True)
    try:
        cur.execute("SELECT Offer.idOffer, title, description, Offer_Contact.email, phone, user_id, salary_aids, salary_total, location, endOffer, first_name, last_name \
                     FROM Offer \
                     NATURAL JOIN Offer_Contact\
                     NATURAL JOIN Offer_Vacancies\
                     NATURAL JOIN Offer_Location\
                     JOIN User ON idUser = userId\
                     LEFT JOIN \
                     (SELECT * FROM Favorite \
                     WHERE Favorite.user_id = %s )  AS my_favorites \
                     ON Offer.idOffer = my_favorites.idOffer\
                     LIMIT 100 ;"%(user_id))
        offers_map = {}
        for (idOffer, title, description, email, phone, user_id, salary_aids, salary_total, location, endOffer, first_name, last_name) in cur:
            offer = offers_map.get(idOffer)
            if offer:
                offer.get('contacts', []).append({'email': email, 'phone': phone})
                offer.get('vacancies', []).append({'salary_aids' : salary_aids, 'salary_total': salary_total})
            else:
                offers_map[idOffer] = {
                        'first_name': first_name,
                        'last_name': last_name,
                        'endOffer': endOffer,
                        'idOffer': idOffer,
                        'title': title,
                        'description': description,
                        'user_favorite' : user_id,
                        'contacts': [{'email': email, 'phone': phone}],
                        'vacancies' : [{'salary_aids' : salary_aids, 'salary_total': salary_total}],
                        'location' : location
                    }
        offers = []
        for offer_id, offer in offers_map.iteritems():
            offers.append(offer)

    except Exception as e:
        return {'success': False, 'error': str(e)}
    finally:
        cur.close()
        cnx.close()

    return {'success': True, 'offers': offers}

def list_offers_by_id(user_id):

    cnx = connect_db()
    cur = cnx.cursor(buffered=True)
    try:
        cur.execute("SELECT Offer.idOffer, title, description, email, phone, salary_aids, salary_total, location  \
                     FROM Offer \
                     NATURAL JOIN Offer_Contact\
                     NATURAL JOIN Offer_Vacancies\
                     NATURAL JOIN Offer_Location\
                     WHERE Offer.userId = %s\
                     LIMIT 100 ;"%(user_id))
        offers_map = {}
        for (idOffer, title, description, email, phone, salary_aids, salary_total, location) in cur:
            offer = offers_map.get(idOffer)
            if offer:
                offer.get('contacts', []).append({'email': email, 'phone': phone})
                offer.get('vacancies', []).append({'salary_aids' : salary_aids, 'salary_total': salary_total})
            else:
                offers_map[idOffer] = {
                        'idOffer': idOffer,
                        'title': title,
                        'description': description,
                        'contacts': [{'email': email, 'phone': phone}],
                        'vacancies': [{'salary_aids' : salary_aids, 'salary_total': salary_total}],
                        'location' : location
                    }
        offers = []
        for offer_id, offer in offers_map.iteritems():
            offers.append(offer)

    except Exception as e:
        return {'success': False, 'error': str(e)}
    finally:
        cur.close()
        cnx.close()

    
    return {'success': True, 'offers': offers}

def insert_offer(offer):
    """ Insert new offer """
    cnx = connect_db()
    
    try:
        cnx.start_transaction()
    
        cur = cnx.cursor(buffered=True)
        
        # Get last iserted id:
        cur.execute("SELECT idOffer FROM Offer ORDER BY idOffer DESC LIMIT 1;")
        
        last_inserted_id = None
        for (idUser) in cur:
            last_inserted_id = str(int(idUser[0] + 1))
            
        if not last_inserted_id:
            last_inserted_id = 1
        
        query = "INSERT INTO Offer VALUES (%s, %s, %s, %s, %s)"
        cur.execute(query, (last_inserted_id, 
                            offer.title, 
                            offer.description, 
                            offer.user_id, 
                            offer.end_offer))
        
        query = "INSERT INTO Offer_Contact VALUES(%s, %s, %s)"    
        cur.execute(query, (offer.email, offer.phone, last_inserted_id))

        query = "INSERT INTO Offer_Vacancies VALUES(%s, %s, %s, %s)"    
        cur.execute(query, (offer.offer_type, offer.salary_aids, offer.salary_total, last_inserted_id))

        query = "INSERT INTO Offer_Location VALUES(%s, %s, %s, %s)"    
        cur.execute(query, (offer.location, last_inserted_id, offer.latitude, offer.longitude))
        
        cnx.commit()
    except Exception as e:
        return {'success': False, 'error': str(e)}
    finally:
        cur.close()
        cnx.close()
        
    new_offer = cur.lastrowid

    return {'success': True, 'inserted_offer': new_offer}

def get_offer(offer_id, user_id):
    """ Get offer by id """
    cnx = connect_db()
    cur = cnx.cursor(buffered=True)

    query = ("SELECT Offer.idOffer, title, description, endOffer, Offer_Contact.email, phone, location, latitude, longitude, salary_aids, salary_total, User.idUser, first_name, last_name\
            FROM Offer\
            LEFT JOIN Offer_Contact ON Offer.idOffer = Offer_Contact.idOffer\
            LEFT JOIN Offer_Location ON Offer.idOffer = Offer_Location.idOffer\
            LEFT JOIN Offer_Vacancies ON Offer.idOffer = Offer_Vacancies.idOffer\
            LEFT JOIN Favorite ON Offer.idOffer = Favorite.idOffer\
            JOIN User ON Offer.userId = User.idUser\
            WHERE Offer.idOffer = %s;"%(offer_id))

    try:
        cur.execute(query)
        offer = {}
        offer_map = {}
        for (idOffer, title, description, endOffer, email, phone, location, latitude, longitude, salary_aids, salary_total, idUser, first_name, last_name) in cur:
            offer = offer_map.get(idOffer)
            if offer:
                offer.get('contacts', []).append({'email': email, 'phone': phone})
                offer.get('vacancies', []).append({'salary_aids':salary_aids, 'salary_total': salary_total})
            else:
                offer_map[idOffer] = {
                    'offer_id': idOffer,
                    'title': title,
                    'description': description,
                    'end_offer': endOffer,
                    'contacts': [{'email': email, 'phone':phone}],
                    'location':location,
                    'latitude':latitude,
                    'longitude':longitude,
                    'vacancies': [{'salary_aids':salary_aids, 'salary_total': salary_total}],
                    'user_id': idUser,
                    'first_name':first_name,
                    'last_name':last_name
                }
        
    except Exception as e:
        return {'success': False, 'error': str(e)}
    finally:
        cur.close()
        cnx.close()

    return {'success': True, 'offer': offer_map.get(offer_id)}

def list_avaliations(offer_id):
        
    cnx = connect_db()
    cur = cnx.cursor(buffered=True)

    try:
        cur.execute("SELECT idAvaliation, date, idOffer, userId, value, text\
                    FROM Avaliation\
                    NATURAL JOIN Rate\
                    NATURAL JOIN Comment\
                    WHERE Avaliation.idOffer = %s ;"%(offer_id))
    
        avaliations = []
        for(idAvaliation, date, idOffer, userId, value, text) in cur:
            avaliations.append(
                {
                    'avaliation_id' : idAvaliation,
                    'date' : date,
                    'offer_id' : idOffer,
                    'user_id' : userId,
                    'rating' : value,
                    'comment' : text
                }
            )

    except Exception as e:
        return {'success' : False, 'error' : str(e)}
    finally:
        cur.close()
    return {'sucess' : True, 'avaliations': avaliations}

def insert_avaliation(avaliation):
    
    cnx = connect_db()
    cur = cnx.cursor(buffered=True)

    try:

        cur.execute("SELECT idAvaliation FROM Avaliation ORDER BY idAvaliation DESC LIMIT 1;")
        last_inserted_id = None
        for (idAvaliation) in cur:
            last_inserted_id = str(int(idAvaliation[0] + 1))
            
        if not last_inserted_id:
            last_inserted_id = 1

        made_querry = 1
        query = "INSERT INTO Avaliation VALUES (" + str(last_inserted_id) + ", %s, %s, %s)"
        cur.execute(query, (avaliation.date,
                            avaliation.offer_id,
                            avaliation.user_id))

        print type(avaliation.offer_id)
        print type(avaliation.user_id)

        made_querry = made_querry + 1
        cur.execute("INSERT INTO Rate VALUES (%s, %s)", (avaliation.value, last_inserted_id))
        made_querry = made_querry + 1
        cur.execute("INSERT INTO Comment VALUES (%s, %s)", (avaliation.text, last_inserted_id))
        cnx.commit()
        
    except Exception as e:
        return {'success' : False, 'error' : str(e), 'last_try' : made_querry}

    finally:
        cur.close()
        cnx.close()

    return {'sucess' : True, 'avaliations': last_inserted_id}