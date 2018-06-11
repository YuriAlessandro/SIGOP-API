from functions.utils import connect_db

def list_offers(user_id):
    """ List all users """
    cnx = connect_db()
    cur = cnx.cursor(buffered=True)
    try:
        cur.execute("SELECT Offer.idOffer, description, email \
                     FROM Offer \
                     NATURAL JOIN Offer_Contact\
                     LEFT JOIN \
                     (SELECT * FROM Favorite \
                     WHERE Favorite.user_id = %s )  AS my_favorites \
                     ON Offer.idOffer = my_favorites.idOffer\
                     LIMIT 100 \
                     OFFSET 0;"%(user_id))
    
    except Exception as e:
        return {'success': False, 'error': str(e)}

    offers = []
    for (idOffer, description, email) in cur:
        offers.append(
                {
                    'idOffer': idOffer,
                    'description': description,
                    'email': email
                }
            )
    cur.close()
    cnx.close()
    return {'success': True, 'offers': offers}

def insert_offer(offer):
    """ Insert new offer """
    cnx = connect_db()
    
    try:
        cnx.start_transaction()
    except Exception as e:
        return {'success': False, 'error': str(e)}
    
    cur = cnx.cursor(buffered=True)

    query = "INSERT INTO Offer VALUES (%s, %s, %s, %s, %s)"
    try:
        cur.execute(query, (offer.offer_id, offer.title, offer.description, offer.user_id, offer.end_offer))
    except Exception as e:
        return {'success': False, 'error': str(e)}

    query = "INSERT INTO Offer_Contact VALUES(%s, %s, %s)"

    try:
        cur.execute(query, (offer.email, offer.phone, offer.offer_id))
    except Exception as e:
        return {'success': False, 'error': str(e)}

    new_offer = cur.lastrowid

    cnx.commit()
    cur.close()
    cnx.close()

    return {'success': True, 'inserted_offer': new_offer}

def get_offer(offer):
    """ Get offer by id """
    pass