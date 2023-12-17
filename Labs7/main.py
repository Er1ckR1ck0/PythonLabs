import flet as ft
from sql_def import *
import logging
from request import url_film

logging.basicConfig(level=logging.INFO)


def main(page: ft.Page):
    link_text = ft.Text()
    
    def button_apply(e):
        add_films(name.value, year.value, rating.value, category.value, director.value, country.value)
        film = ft.Dropdown(
            width=300,
            options=[ft.dropdown.Option(get_film_by_name()[i]) for i in range(0, len(get_film_by_name()) )],
        )
        dlg.open = False
        page.update()
    def button_apply_info(e):
        add_info_DB(delete_film.value, country.value, cash.value)
        film = ft.Dropdown(
            width=300,
            options=[ft.dropdown.Option(get_film_by_name()[i]) for i in range(0, len(get_film_by_name()) )],
        )
        add_info.open = False
        page.update()
    def add_button_clicked(e):
        page.dialog = dlg
        dlg.open = True
        
        page.update()
    def add_info_button_clicked(e):
        page.dialog = add_info
        add_info.open = True
        
        page.update()
    def delete_button_clicked(e):
        page.dialog = dlg_delete
        dlg_delete.open = True
        
        page.update()

    def apply_deletes(e):
        delete_films(delete_film.value)
        film = ft.Dropdown(
            width=300,
            options=[ft.dropdown.Option(get_film_by_name()[i]) for i in range(0, len(get_film_by_name()) )],
        )
        film.update()
        dlg_delete.open = False
        page.update()
    def delete_info_apply(e):
        delete_info_DB(delete_film.value)
    
        add_info.open = False
        page.update()

    def show_money(e):
        output_text.value = f"Информация о cборах фильма {film.value}:\n\n{get_films_money(film.value)}\n\n"
        link_text.spans = [
            ft.TextSpan(
                    "Посмотреть фильм",
                    ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE),
                    url=url_film(film.value),
                ),
        ]
        show_money_btn = ft.ElevatedButton(text="Посмотреть сборы", on_click=show_money)
        page.update()
    def close_dlg(e):
        dlg.open = False
        page.update()
    def button_clicked(e):
        output_text.value = f"Информация о фильме:\n\n{get_films(film.value)}\n\n"
        link_text.spans = [
            ft.TextSpan(
                    "Посмотреть фильм",
                    ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE),
                    url=url_film(film.value),
                ),
        ]
        page.update()
    
    show_money_btn = ft.ElevatedButton(text="Посмотреть сборы", on_click=show_money)
    output_text = ft.Text(
        size=24,
        color=ft.colors.WHITE,
    )
    add_button = ft.ElevatedButton(text="+", on_click=add_button_clicked, color=ft.colors.AMBER, width=64, height=64, scale=ft.Scale(0.75))
    add_info_button = ft.ElevatedButton(text='Добавить сборы', on_click=add_info_button_clicked)
    delete_button = ft.ElevatedButton(text="-", on_click=delete_button_clicked, color=ft.colors.AMBER, width=64, height=64, scale=ft.Scale(0.75))
    submit_btn = ft.ElevatedButton(text="Принять", on_click=button_clicked)
    film = ft.Dropdown(
        width=300,
        options=[ft.dropdown.Option(get_film_by_name()[i]) for i in range(0, len(get_film_by_name()) )],
    )
    name = ft.TextField(label="Название фильма",  width=500, error_text="Название не может быть пустым", error_style=ft.TextStyle(color=ft.colors.RED))
    year = ft.TextField(label="Год выпуска", width=500,)
    rating = ft.TextField(label="Рейтинг", width=500,)
    category = ft.TextField(label="Категория", width=500)
    director = ft.TextField(label="Режиссер", width=500)
    country = ft.TextField(label="Страна", width=500)
    cash = ft.TextField(label="Кассовые сборы", width=500)
    delete_film = ft.Dropdown(
        width=300,
        options=[ft.dropdown.Option(get_film_by_name()[i]) for i in range(0, len(get_film_by_name()))],
        )
    dlg_delete = ft.AlertDialog(title= ft.Text("Удалить запись"), content=ft.Column(width=500,controls=[delete_film,
        ft.ElevatedButton(text="Удалить", on_click=apply_deletes)]),
        on_dismiss=lambda e: print("Не получилось создать запись"))
    add_info = ft.AlertDialog(
        title=ft.Text("Добавить запись"), content=ft.Column(width=500,controls=[delete_film, country, cash,
                    ft.Row(controls=[ft.ElevatedButton(text="Создать", on_click=button_apply_info),
                    ft.ElevatedButton(text="Удалить", on_click=delete_info_apply, color=ft.colors.RED)])]), on_dismiss=lambda e: print("Не получилось создать запись")
    )
    dlg = ft.AlertDialog(
        title=ft.Text("Добавить запись"), content=ft.Column(width=500,controls=[name, year, rating, category, director, country,
                    ft.Row(controls=[ft.ElevatedButton(text="Создать", on_click=button_apply),
                    ft.ElevatedButton(text="Отмена", on_click=close_dlg, color=ft.colors.RED)])]), on_dismiss=lambda e: print("Не получилось создать запись")
    )
    page.add(ft.Row(controls=[film, add_button, add_info_button, delete_button]), ft.Row(controls=[submit_btn, show_money_btn]),  output_text, link_text)

ft.app(target=main)