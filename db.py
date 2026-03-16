import mysql.connector

def get_connection():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Pearlin@2006",
        database="project_portal"
    )

    return conn