class Film: 
    def __init__(self, name, code, director, year, actors):
        self.name = name
        self.code = code #default
        self.director = director #default (♥ Tarantino)
        self.year   = year
        self.actors = actors

    def print_method(self):
        print(self.name, self.code, self.director, self.year, self.actors)


class FilmManagment:
    def __init__(self):
        self.list_objects = []

    def add_films(self):
        name = input("> Введите название фильма: ")
        code = int(input("> Введите номер кода: "))
        director = input("> Введите режиссера: ")
        year = int(input("> Введите год выпуска: "))
        actors = input("> Введите актеров: ")
        return Film(name, code, director, year, actors)
    def delete_films(self):
        code = int(input("> Введите код удаляемого фильма: "))
        for i in self.list_objects:
            if i.code == code:
                self.list_objects.remove(i)
                break

    def show_films(self):
        print(self.list_objects)

def check(input_number):
    while not input_number.isdigit() or int(input_number) > 3:
        input_number = input("> Plese, write your number: ")
    return input_number


def main():
    list_objects = []
    
    # match input_number:
    #     case 
    while input_number != 0:
        input_number = int(check(input("> Plese, write your number: ")))
        if input_number == 1:
            list_objects.append(FilmManagment().add_films())
            print(list_objects)
            input_number = int(check(input("> Plese, write your number: ")))
        if input_number == 2:
            for i in list_objects:
                list_objects[i]
                

if __name__ == "__main__":
    main()