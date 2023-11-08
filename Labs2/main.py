class Film:
    def __init__(self, code, title, director, release_year, actors):
        self.code = code
        self.title = title
        self.director = director
        self.release_year = release_year
        self.actors = actors

class FilmManagement:
    def __init__(self):
        self.film_list = []

    def add_film(self, code, title, director, release_year, actors):
        film = Film(code, title, director, release_year, actors)
        self.film_list.append(film)

    def delete_film(self, code):
        for film in self.film_list:
            if film.code == code:
                self.film_list.remove(film)
                break

    def display_all_films(self):
        for film in self.film_list:
            print("Code:", film.code)
            print("Title:", film.title)
            print("Director:", film.director)
            print("Release Year:", film.release_year)
            print("Actors:", ", ".join(film.actors))
            print()

    def search_films_by_release_year(self, release_year):
        for film in self.film_list:
            if film.release_year == release_year:
                print("Code:", film.code)
                print("Title:", film.title)
                print("Director:", film.director)
                print("Release Year:", film.release_year)
                print("Actors:", ", ".join(film.actors))
                print()

def main():
    film_management = FilmManagement()

    while True:
        print("1. Add Film")
        print("2. Delete Film")
        print("3. Display All Films")
        print("4. Search Films by Release Year")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            code = input("Enter the film code: ")
            title = input("Enter the film title: ")
            director = input("Enter the director: ")
            release_year = int(input("Enter the release year: "))
            actors = input("Enter the actors (comma-separated): ").split(",")
            film_management.add_film(code, title, director, release_year, actors)
        elif choice == "2":
            code = input("Enter the film code: ")
            film_management.delete_film(code)
        elif choice == "3":
            film_management.display_all_films()
        elif choice == "4":
            release_year = int(input("Enter the release year: "))
            film_management.search_films_by_release_year(release_year)
        elif choice == "5":
            break

if __name__ == "__main__":
    main()