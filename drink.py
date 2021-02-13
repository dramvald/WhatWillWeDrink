import requests
import json
from prettytable import PrettyTable
import re


ALCOHOL = 'Alcoholic'
RANDOM_DRINK_API_URL = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
INGREDIENT = r'^strIngredient.'
MEASURE = r'^strMeasure.'


def get_drink_data(RANDOM_DRINK_API_URL):
    # Делам запрос на сервер по адресу req_url.
    # Преобразуем строку json в объект python типа dict.
    data = requests.get(RANDOM_DRINK_API_URL).json()

    def get_instructions_measures():
        # Эта функция позволяет автоматически искать и заносит в список ингредиенты, и их количество
        ingredient = []
        measure = []
        for key in data['drinks']:
            for x, y in key.items():
                if re.match(INGREDIENT, x):
                    ingredient.append(y)
                if re.match(MEASURE, x):
                    measure.append(y)
        return ingredient, measure
    ingredients, measure = get_instructions_measures()
    # Так как содержимое ключа drinks имеет тип list,
    # использую for для того чтобы пройтись по элементам списка,
    # которые являются словарями, и взять нужные данные.
    for item in data['drinks']:
        drink = item['strDrink']
        instruction = item['strInstructions']

        # Уменьшаю список убирая в ingredients и measure элементы имеющие None.
        ingredients = list(filter(None, ingredients))
        measure = list(filter(None, measure))
        # Делаю проверку на алкогольный или без алкогольный напиток, и если он без алкогольный,
        # то отправляется снова запрос и проходит по циклу.
        if ALCOHOL != item['strAlcoholic']:
            return get_drink_data(RANDOM_DRINK_API_URL)
        else:
            return drink, instruction, ingredients, measure


def show_drink(drink, instruction, ingredients, measure):
    # Создал функцию для создания таблицы.
    p = PrettyTable()
    p.add_column('Drink name', [drink])
    p.add_column('Drink sign', [ALCOHOL])
    p.add_column('Instructions for preparation', [instruction])
    p.add_column('Ingredients', [ingredients])
    p.add_column('Ingredient quantity', [measure])
    print(p.get_string())

# drink, instruction, ingredients, measure = get_drink_data(req_url)
# show_drink(drink, instruction, ingredients, measure)
