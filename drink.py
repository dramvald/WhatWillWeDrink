import requests
import json
from prettytable import PrettyTable
from queue import PriorityQueue

ALCOHOL = 'Alcoholic'
RANDOM_DRINK_API_URL = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
INGREDIENT = 'strIngredient'
MEASURE = 'strMeasure'


def get_drink_data(RANDOM_DRINK_API_URL):
    """Делам запрос на сервер по адресу req_url.
    Преобразуем строку json в объект python типа dict."""
    data = requests.get(RANDOM_DRINK_API_URL).json()
    # Так как содержимое ключа drinks имеет тип list,
    # использую for для того чтобы пройтись по элементам списка,
    # которые являются словарями, и взять нужные данные.
    for item in data['drinks']:
        drinks = item['strDrink']
        instruction = item['strInstructions']
        # Делаю проверку на алкогольный или без алкогольный напиток, и если он без алкогольный,
        # то отправляется снова запрос и проходит по циклу.
        if ALCOHOL != item['strAlcoholic']:
            return get_drink_data(RANDOM_DRINK_API_URL)
        else:
            return drinks, instruction, data['drinks'][0]


def sort_values(drinks, property_name):
    """Эта функция позволяет автоматически найти и записать данные искомых значений"""
    pq = PriorityQueue()
    for key, value in drinks.items():
        if isinstance(key, str) and key.startswith(property_name):
            if value is not None:
                # Уменьшаю список убирая элементы имеющие None.
                pq.put((int(key[-1]), value))
    return [i[1] for i in pq.queue]


def show_drink(drinks, instruction, ingredients, measure):
    """Функция для создания таблицы."""
    p = PrettyTable()

    p.add_column('Drink name', [drinks])
    p.add_column('Drink sign', [ALCOHOL])
    p.add_column('Instructions for preparation', [instruction])
    p.add_column('Ingredients', [ingredients])
    p.add_column('Ingredient quantity', [measure])
    print(p.get_string())

