import mysql.connector

def connect_db():
    """ Connect to database"""
    connection = mysql.connector.connect(user='admin', password='senha',
                                         host='127.0.0.1',
                                         database='sigopdb')

    return connection