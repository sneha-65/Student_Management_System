import mysql.connector

def get_connection():

    return mysql.connector.connect(

        host="localhost",
        user="root",
        password="Mysql6537@js",
        database="student_management"

    )