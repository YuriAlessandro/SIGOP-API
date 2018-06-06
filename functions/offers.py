from functions.utils import connect_db

def list_offers():
    """ List all users """
    cnx = connect_db()
    cur = cnx.cursor(buffered=True)
    try:
        cur.execute("SELECT description, email\
                     FROM Offer\
                     NATURAL JOIN Offer_Contact\
                     LEFT JOIN \
                        (SELECT * FROM Favorite \
                         WHERE Favorite.user_id = 1) AS my_favorites\
                     ON my_favorites.offer_id = Offer.idOffer\
                     LIMIT 100 \
                     OFFSET 0;")
    
    except Exception as e:
        return {'success': False, 'error': str(e)}

    offers = []
    for (description, email) in cur:
        offers.append(
                {
                    'description': description,
                    'email': email,
                }
            )
    cur.close()
    cnx.close()
    return {'success': True, 'offers': offers}
