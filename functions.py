import mysql.connector

from models.user import User

def connect_db():
    """ Connect to database"""
    connection = mysql.connector.connect(user='admin', password='senha',
                                         host='127.0.0.1',
                                         database='sigopdb')

    return connection

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
    return users

def insert_user(user):
    """ Create a new user """
    cnx = connect_db()
    cur = cnx.cursor(buffered=True)

    query = "INSERT INTO User VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"

    try:
        cur.execute(query, (user.user_id,
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

    new_user = cur.lastrowid

    cnx.commit()
    cur.close()
    cnx.close()

    return {'success': True, 'inserted_user': new_user}

