# try outs on mysqlite3
import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS myusers (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

user = (1, 'marcel', 'abcd')
insert_query = "INSERT INTO myusers VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

users = [
    (2, 'bruce', 'abcd'),
    (3, 'lee', 'abcd'),
]
cursor.executemany(insert_query, users)

select_query = "SELECT * FROM myusers"
for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()
