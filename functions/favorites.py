from functions.utils import connect_db

def list_favorites(user_id):
    """ List all favorites from user """
    cnx = connect_db()
    cur = cnx.cursor(buffered=True)
    try:
        cur.execute("SELECT Offer.idOffer, title, description, email, phone, salary_aids, salary_total, location \
                     FROM Offer \
                     NATURAL JOIN Offer_Contact\
                     NATURAL JOIN Offer_Vacancies\
                     NATURAL JOIN Offer_Location\
                     JOIN \
                     (SELECT * FROM Favorite \
                     WHERE Favorite.user_id = %s )  AS my_favorites \
                     ON Offer.idOffer = my_favorites.idOffer\
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


    return {'success': True, 'Favorites': offers}

def insert_favorite(favorite):
    """ Insert new favorite """
    cnx = connect_db()
    
    try:
        cnx.start_transaction()
    
        cur = cnx.cursor(buffered=True)

        query = "INSERT INTO Favorite VALUES ( %s, %s)"
        cur.execute(query, (favorite.user_id, favorite.offer_id))

        cnx.commit()
    except Exception as e:
        return {'success': False, 'error': str(e)}
    finally:
        cur.close()
        cnx.close()

    return {'success': True, 'inserted_new_favorite_offer': favorite.offer_id}
