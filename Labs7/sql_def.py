import sqlite3
con = sqlite3.connect("Films.db", check_same_thread=False )
cur = con.cursor()

def get_info():
    cur.execute("SELECT * FROM Films")
    rows = cur.fetchall()
    films = []
    for row in rows:
        films.append(row)
    return films

def get_films(naming):
    cur.execute("SELECT * FROM Films where name = ?", (naming,))
    rows = cur.fetchall()
    id, name, year, rating, category, director, country = str(), str(), str(), str(), str(), str(), str()
    for row in rows:
        id = row[0]
        name = row[1]
        year = row[2]
        rating = row[3]
        category = row[4]
        director = row[5]
        country = row[6]
    return f"{name}, {year}, {rating}, {category}, {director}, {country}"

def get_films_money(naming):
    id = cur.execute("SELECT id FROM Films where name = ?", (naming,)).fetchall()[0][0]
    cur.execute("SELECT * FROM Money where id_movie = ?", (id,))
    rows = cur.fetchall()
    country, cash, text = str(), str(), str()
    for row in rows:
        print(row)
        country, cash = row[2], row[3]
        print(row[2])
        text += f"{country}: {cash}\n"
    return text
def get_film_by_name():
    cur.execute("SELECT * FROM Films")
    rows = cur.fetchall()
    id, name, year, rating, category, director, country = [], [], [], [], [], [], []
    for row in rows:
        name.append(row[1])
    return name

def add_films(name, year, rating, category, director, country):
    cur.execute("Insert into Films (name, year, rating, category, director, country) Values(?, ?, ?, ?, ?, ?)", (name, year, rating, category, director, country))
    con.commit()
    
def delete_films(name):
    id = cur.execute("SELECT id FROM Films where name = ?", (name,)).fetchall()[0][0]
    print(id)

    print(cur.execute("SELECT * FROM Films where id = ?", (id,)).fetchall())
    cur.execute("DELETE FROM Films where id = ?", (id,))
    con.commit()
    