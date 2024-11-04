import sqlite3
import os

path = "./data.dat"
database = "agenda.db"
datas = []
if os.path.isfile(path):
    with open(path, "r") as file:
        nome: str = ""
        telefone: str = ""
        for i,linha in enumerate(file.readlines()):
            if i%2 == 0:
                nome = str(linha).rstrip('\n')
            else:
                telefone = str(linha).rstrip('\n')
                datas.append((nome, telefone))
    if os.path.isfile(database):
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        cursor.executemany('''
            insert into agenda (nome, telefone) values (?, ?)
        ''', datas)
        connection.commit()
        cursor.close()
        connection.close()
    else:
        print("Banco agenda.db não existe!")
else:
    print("Arquivo data.dat não existe!")