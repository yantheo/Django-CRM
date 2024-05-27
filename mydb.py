import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
)

# Prepare a cursor objet
cursorObjet = dataBase.cursor()

# Create database
cursorObjet.execute("CREATE DATABASE djangocrm")
print("ALL DONE!!!")
