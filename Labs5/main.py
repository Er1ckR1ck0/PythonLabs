import tkinter as tk
from tkinter import messagebox
import json

class Film:
    def __init__(self, code, title, director, release_year, actors):
        self.code = code
        self.title = title
        self.director = director
        self.release_year = release_year
        self.actors = actors

class FilmManagement:
    def __init__(self):
        self.films = []

    def add_film(self, code, title, director, release_year, actors):
        new_film = Film(code, title, director, release_year, actors)
        self.films.append(new_film)

    def delete_film(self, code):
        for film in self.films:
            if film.code == code:
                self.films.remove(film)
                break

    def display_films(self):
        for film in self.films:
            print(f"Код: {film.code}, Название: {film.title}, Режиссёр: {film.director}, Год выпуска: {film.release_year}, Актеры: {', '.join(film.actors)}")

    def search_films(self, release_year):
        result = []
        for film in self.films:
            if film.release_year == release_year:
                result.append(film)
        return result

    def save_films(self, filename):
        with open(filename, 'w') as file:
            json.dump([film.__dict__ for film in self.films], file)

    def load_films(self, filename):
        try:
            with open(filename, 'r') as file:
                films_data = json.load(file)
                self.films = [Film(**film) for film in films_data]
        except FileNotFoundError:
            pass

class LabWorkInterface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Лабораторная работа № 3")

        # Надписи
        title_label = tk.Label(self.window, text="Лабораторная работа № 3")
        title_label.pack()

        # Текстовые поля
        code_label = tk.Label(self.window, text="Код:")
        code_label.pack()
        self.code_entry = tk.Entry(self.window)
        self.code_entry.pack()

        title_label = tk.Label(self.window, text="Название:")
        title_label.pack()
        self.title_entry = tk.Entry(self.window)
        self.title_entry.pack()

        director_label = tk.Label(self.window, text="Режиссёр:")
        director_label.pack()
        self.director_entry = tk.Entry(self.window)
        self.director_entry.pack()

        release_year_label = tk.Label(self.window, text="Год выпуска:")
        release_year_label.pack()
        self.release_year_entry = tk.Entry(self.window)
        self.release_year_entry.pack()

        actors_label = tk.Label(self.window, text="Актеры:")
        actors_label.pack()
        self.actors_entry = tk.Entry(self.window)
        self.actors_entry.pack()

        # Кнопки
        add_button = tk.Button(self.window, text="Добавить", command=self.add_film)
        add_button.pack()

        delete_button = tk.Button(self.window, text="Удалить", command=self.delete_film)
        delete_button.pack()

        display_button = tk.Button(self.window, text="Отобразить", command=self.display_films)
        display_button.pack()

        search_button = tk.Button(self.window, text="Поиск", command=self.search_films)
        search_button.pack()

        save_button = tk.Button(self.window, text="Сохранить", command=self.save_films)
        save_button.pack()

        load_button = tk.Button(self.window, text="Загрузить", command=self.load_films)
        load_button.pack()

        self.window.mainloop()

    def add_film(self):
        code = self.code_entry.get()
        title = self.title_entry.get()
        director = self.director_entry.get()
        release_year = self.release_year_entry.get()
        actors = self.actors_entry.get().split(",")
        print(code, title, director, release_year, actors)
        film_management = FilmManagement()
        film_management.add_film(code, title, director, release_year, actors)
        print(film_management.display_films())

    def delete_film(self):
        code = self.code_entry.get()

        film_management = FilmManagement()
        film_management.delete_film(code)

    def display_films(self):
        film_management = FilmManagement()
        film_management.display_films()

    def search_films(self):
        release_year = self.release_year_entry.get()

        film_management = FilmManagement()
        result = film_management.search_films(release_year)

        if result:
            for film in result:
                print(f"Код: {film.code}, Название: {film.title}, Режиссёр: {film.director}, Год выпуска: {film.release_year}, Актеры: {', '.join(film.actors)}")
        else:
            print("Фильмы не найдены")

    def save_films(self):
        film_management = FilmManagement()
        film_management.save_films("films.json")
        messagebox.showinfo("Сохранение", "Фильмы сохранены.")

    def load_films(self):
        film_management = FilmManagement()
        film_management.load_films("films.json")
        messagebox.showinfo("Загрузка", "Фильмы загружены.")

interface = LabWorkInterface()