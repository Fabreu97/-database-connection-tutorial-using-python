import sqlite3
import os
path = './agenda.db'
if os.path.isfile(path):
    connection = sqlite3.connect("agenda.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM agenda")
    res = cursor.fetchall()
    print("")
    for line in res:
        print(f"Nome: {line[0]}\nTelefone: {line[1]}\n")
    cursor.close()
    connection.close()
else:
    print("O banco agenda.db não existe!")