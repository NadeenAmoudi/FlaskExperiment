import sqlite3

conn = sqlite3.connect('database.db')

conn.execute('CREATE TABLE chapter (id integer primary key autoincrement, name string not null, description string not null, chapterNum integer, pageNum integer)')

conn.close()

