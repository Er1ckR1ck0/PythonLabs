import sqlite3

con = sqlite3.connect("Films.db", check_same_thread=False)
cur = con.cursor()
cur.execute(""" drop table if exists Films """)
cur.execute("""
        Create Table IF NOT EXISTS Films (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            year INTEGER,
            rating REAL,
            category TEXT,
            director TEXT,
            country TEXT
        )""")

cur.execute("""
    CREATE TABLE if not exists Money (
        id INTEGER PRIMARY KEY,
        id_movie INTEGER,
        country TEXT,
        cash TEXT
    )""")

#Заполняем таблицу
#ФИЛЬМЫ
cur.execute("""
            Insert into Films (id, name, year, rating, category, director, country)
            Values(?, ?, ?, ?, ?, ?, ?)""", (1, "The Godfather", 1972, 9.2, "Crime", "Francis Ford Coppola", "USA"))
cur.execute("""
            Insert into Films (id, name, year, rating, category, director, country)
            Values(?, ?, ?, ?, ?, ?, ?)""", (2, "The Godfather: Part II", 1974, 9.0, "Crime", "Francis Ford Coppola", "USA"))

cur.execute("""
            Insert into Films (id, name, year, rating, category, director, country)
            Values(?, ?, ?, ?, ?, ?, ?)""", (3, "The Dark Knight", 2008, 9.0, "Action", "Christopher Nolan", "USA"))

cur.execute("""
            Insert into Films (id, name, year, rating, category, director, country)
            Values(?, ?, ?, ?, ?, ?, ?)""", (4, "Pulp Fiction", 1994, 8.9, "Crime", "Quentin Tarantino", "USA"))

cur.execute("""
            Insert into Films (id, name, year, rating, category, director, country)
            Values(?, ?, ?, ?, ?, ?, ?)""", (5, "Kill Bill", 2003, 8.9, "Crime", "Quentin Tarantino", "USA"))


#Сборы в странах
cur.execute("""
            Insert into Money (id, id_movie, country, cash)
            Values(?, ?, ?, ?);""", (1, 1, 'USA', '100000$'))
cur.execute("""
            Insert into Money (id, id_movie, country, cash)
            Values(?, ?, ?, ?);""", (2, 1, 'UK', '231349$'))
cur.execute("""
            Insert into Money (id, id_movie, country, cash)
            Values(?, ?, ?, ?);""", (3, 1,'Russia', '123899$'))

cur.execute("""
            Insert into Money (id, id_movie, country, cash)
            Values(?, ?, ?, ?);""", (4, 2, 'USA', '789920$'))
cur.execute("""
            Insert into Money (id, id_movie, country, cash)
            Values(?, ?, ?, ?);""", (5, 2, 'UK', '139800$'))
cur.execute("""
            Insert into Money (id, id_movie, country, cash)
            Values(?, ?, ?, ?);""", (6, 2,'Russia', '90421$'))
cur.execute("""
            Insert into Money (id, id_movie, country, cash)
            Values(?, ?, ?, ?);""", (7, 3, 'USA', '2930000$'))
cur.execute("""
            Insert into Money (id, id_movie, country, cash)
            Values(?, ?, ?, ?);""", (8, 3, 'UK', '213000$'))
cur.execute("""
            Insert into Money (id, id_movie, country, cash)
            Values(?, ?, ?, ?);""", (9, 3,'Russia', '188732$'))
cur.execute("""
            Insert into Money (id, id_movie, country, cash)
            Values(?, ?, ?, ?);""", (10, 4, 'USA', '1000000$'))
cur.execute("""
            Insert into Money (id, id_movie, country, cash)
            Values(?, ?, ?, ?);""", (11, 4, 'UK', '489992$'))
cur.execute("""
            Insert into Money (id, id_movie, country, cash)
            Values(?, ?, ?, ?);""", (12, 4,'Russia', '299102$'))
cur.execute("""
            Insert into Money (id, id_movie, country, cash)
            Values(?, ?, ?, ?);""", (13, 5, 'USA', '2000312$'))
cur.execute("""
            Insert into Money (id, id_movie, country, cash)
            Values(?, ?, ?, ?);""", (14, 5, 'UK', '758834$'))
cur.execute("""
            Insert into Money (id, id_movie, country, cash)
            Values(?, ?, ?, ?);""", (15, 5,'Russia', '327775$'))

con.commit()