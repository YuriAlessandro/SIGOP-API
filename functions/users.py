# -*- coding: utf-8 -*-
from functions.utils import connect_db
from models.user import User

def auth(username, password):
    cnx = connect_db()
    cur = cnx.cursor(buffered=True)

    query = "SELECT idUser, first_name, last_name, status, login, email, type, unity \
             FROM User\
             WHERE login = %s AND password = %s"
    try:
        cur.execute(query, (username, password))
    except Exception as e:
        return {'success' : False, 'error' : str(e)}
    
    user = {}
    for (idUser, first_name, last_name, status, login, email, type, unity) in cur:
        user = {
            'idUser' : idUser,
            'first_name': first_name,
            'last_name': last_name,
            'status': status,
            'login': login,
            'email': email,
            'type': type,
            'unity': unity }
    
    if not user:
        return {'success': False, 'msg': u'Credenciais inválidas'}
    
    return {"success" : True, 'user' : user}
def list_users():
    """ List all users """
    cnx = connect_db()
    cur = cnx.cursor(buffered=True)
    try:
        cur.execute("SELECT idUser, first_name, last_name, status, login, email, type, unity from User")
    except Exception as e:
        return {'success': False, 'error': str(e)}

    users = []
    for (idUser, first_name, last_name, status, login, email, type, unity) in cur:
        users.append(
                {
                    'user_id': idUser,
                    'first_name': first_name,
                    'last_name': last_name,
                    'status': status,
                    'login': login,
                    'email': email,
                    'type': type,
                    'unity': unity
                }
            )

    cur.close()
    cnx.close()
    return {'success': True, 'users': users}

def insert_user(user):
    """ Create a new user """
    cnx = connect_db()
    cur = cnx.cursor(buffered=True)

    if user.user_type == 'concedente':
        query = "INSERT INTO User VALUES(LAST_INSERT_ID() + 1, %s, %s, %s, %s, %s, %s, %s, %s)"

        try:
            cur.execute(query, (#user.user_id,
                                user.first_name,
                                user.last_name,
                                user.status,
                                user.login,
                                user.email,
                                user.password,
                                user.user_type,
                                user.unity))
        except Exception as e:
            return {'success': False, 'error': str(e)}
    else:
        return {'success': False, 'error': 'must be concedente type'}

    new_user = cur.lastrowid

    cnx.commit()
    cur.close()
    cnx.close()

    return {'success': True, 'inserted_user': new_user}

def get_user(user_id):
    """ Get a user """
    cnx = connect_db()
    cur = cnx.cursor(buffered=True)
    query = ("SELECT idUser, first_name, last_name, status, login, email, type, unity "
             "FROM User "
             "WHERE idUser = %s"% (user_id))

    try:
        print user_id
        cur.execute(query)
    except Exception as e:
        print e
        return {'success': False, 'error': str(e)}

    user = {}
    for (idUser, first_name, last_name, status, login, email, type, unity) in cur:
        user = {
                'user_id': idUser,
                'first_name': first_name,
                'last_name': last_name,
                'status': status,
                'login': login,
                'email': email,
                'type': type,
                'unity': unity
            }
            

    cur.close()
    cnx.close()
    return {'success': True, 'user': user}

