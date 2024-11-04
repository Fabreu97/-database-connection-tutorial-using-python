import sqlite3
connection = sqlite3.connect("agenda.db")
cursor = connection.cursor()
cursor.execute('''
                create table agenda(
                    nome        text,
                    telefone    text)
               ''')
cursor.execute('''
        insert into agenda (nome, telefone) values (?, ?)
''', ('Pablo', '(41)45454-4545'))
connection.commit()
cursor.close()
connection.close()