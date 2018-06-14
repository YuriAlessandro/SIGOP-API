from functions.utils import connect_db

def list_offers(user_id):
    """ List all users """
    cnx = connect_db()
    cur = cnx.cursor(buffered=True)
    try:
        cur.execute("SELECT Offer.idOffer, description, email, phone \
                     FROM Offer \
                     NATURAL JOIN Offer_Contact\
                     LEFT JOIN \
                     (SELECT * FROM Favorite \
                     WHERE Favorite.user_id = %s )  AS my_favorites \
                     ON Offer.idOffer = my_favorites.idOffer\
                     LIMIT 100 ;"%(user_id))
    

    except Exception as e:
        return {'success': False, 'error': str(e)}
    finally:
        cur.close()
        cnx.close()

    offers_map = {}
    for (idOffer, description, email, phone) in cur:
        offer = offers_map.get(idOffer)
        if offer:
            offer.get('contacts', []).append({'email': email, 'phone': phone})
        else:
            offers_map[idOffer] = {
                    'idOffer': idOffer,
                    'description': description,
                    'contacts': [{'email': email, 'phone': phone}]
                }
    offers = []
    for offer_id, offer in offers_map.iteritems():
        offers.append(offer)

    return {'success': True, 'offers': offers}

def insert_offer(offer):
    """ Insert new offer """
    cnx = connect_db()
    
    try:
        cnx.start_transaction()
    
        cur = cnx.cursor(buffered=True)
        
        query = "INSERT INTO Offer VALUES (LAST_INSERT_ID() + 1, %s, %s, %s, %s)"
        cur.execute(query, (#offer.offer_id, 
                            offer.title, 
                            offer.description, 
                            offer.user_id, 
                            offer.end_offer))
        
        query = "INSERT INTO Offer_Contact VALUES(%s, %s, %s)"    
        cur.execute(query, (offer.email, offer.phone, offer.offer_id))
        
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
        
    except Exception as e:
        return {'success': False, 'error': str(e)}
    finally:
        cur.close()
        cnx.close()


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
   
    return {'success': True, 'offer': offer_map.get(offer_id)}
