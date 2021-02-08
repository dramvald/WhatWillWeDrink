import requests
import json
import traceback
from prettytable import PrettyTable

ALCOHOL = 'Alcoholic'
try:
    # req_url адрес сервера
    req_url = "https://www.thecocktaildb.com/api/json/v1/1/random.php"


    def interpellation(req_url):
        # Делам запрос на сервер по адресу req_url.
        resp = requests.get(req_url).text
        # Преобразуем строку json в объект python типа dict.
        date = json.loads(resp)
        # Так как содержимое ключа drinks имеет тип list,
        # использую for для того чтобы пройтись по элементам списка,
        # которые являются словарями, и взять нужные данные.
        for item in date['drinks']:
            drink = item['strDrink']
            instruction = item['strInstructions']
            ingredients = item['strIngredient1'], item['strIngredient2'], item['strIngredient3'], \
                          item['strIngredient4'], item['strIngredient5'], item['strIngredient6'], \
                          item['strIngredient7'], item['strIngredient8'], item['strIngredient9'], \
                          item['strIngredient10'], item['strIngredient11'], item['strIngredient12'], \
                          item['strIngredient13'], item['strIngredient14'], item['strIngredient15']
            measure = item['strMeasure1'], item['strMeasure2'], item['strMeasure3'], \
                      item['strMeasure4'], item['strMeasure5'], item['strMeasure6'], \
                      item['strMeasure7'], item['strMeasure8'], item['strMeasure9'], \
                      item['strMeasure10'], item['strMeasure11'], item['strMeasure12'], \
                      item['strMeasure13'], item['strMeasure14'], item['strMeasure15']
            # Уменьшаю список убирая в ingredients и measure элементы имеющие None.
            ingredients = list(filter(None, ingredients))
            measure = list(filter(None, measure))
            # Делаю проверку на алкогольный или без алкогольный напиток, и если он без алкогольный,
            # то отправляется снова запрос и проходит по циклу.
            if ALCOHOL != item['strAlcoholic']:
                interpellation(req_url)
            else:
                return drink, instruction, ingredients, measure


    def conclusion(drink, instruction, ingredients, measure):
        p = PrettyTable()
        p.add_column('Drink name', [drink])
        p.add_column('Drink sign', [ALCOHOL])
        p.add_column('Instructions for preparation', [instruction])
        p.add_column('Ingredients', [ingredients])
        p.add_column('Ingredient quantity', [measure])
        print(p.get_string())


    #drink, instruction, ingredients, measure = interpellation(req_url)
    #conclusion(drink, instruction, ingredients, measure)
# Здесь работа над ошибкой, когда отсутствует интернет.
except ConnectionError:
    print('Нет соединения с интернетом')
# Здесь работа над всеми остальными ошибками которые возникают в ходе программы.
except Exception as e:
    print('Ошибка:\n', traceback.format_exc())
    print()
