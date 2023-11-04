import requests
from bs4 import BeautifulSoup


def url_film(name):
    try:
        name = name.split(" ")
        new_name = ""
        for i in range(0,len(name)):
            if i == len(name)-1:
                new_name += name[i]
                break
            new_name += name[i]+"+"
        url = f'https://www.kinopoisk.ru/index.php?kp_query={new_name}'
        print(url)
        response = requests.get(url)
        data = BeautifulSoup(response.text, 'html.parser')


        film = data.find('p', class_="name").a["data-id"]


        return f"https://movielab.fun/movies/{film}"
    except:
        return "Фильм не найден"

