import requests
import json
import tableprint as tp
import numpy as np
import traceback

try:
    # req_url адрес сервера
    req_url = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
    def reqs(req_url):
        # Делам запрос на сервер по адресу req_url.
        resp = requests.get(req_url).text
        # Преобразуем строку json в обьект python типа dict.
        date = json.loads(resp)
        # Так как содержимае ключа drinks имеет тип list,
        # использую for для того чтобы пройтись по элементам списка,
        # которые являються словорями, и взять нужные данные.
        for item in date['drinks']:
            alcohol = item['strAlcoholic']
            drink = item['strDrink']
            instruction = item['strInstructions']
            ingredients = item['strIngredient1'], item['strIngredient2'], item['strIngredient3'], \
                          item['strIngredient4'], item['strIngredient5'], item['strIngredient6'], \
                          item['strIngredient7'], item['strIngredient8'], item['strIngredient9'], \
                          item['strIngredient10'], item['strIngredient11'], item['strIngredient12'], \
                          item['strIngredient13'], item['strIngredient14'], item['strIngredient15']
            # делаю проверку на алкогольный или без алкогольный напиток, и если он без алкогольный,
            # то отправляеться сново запрос и проходит по циклу
            if alcohol != 'Alcoholic':
                print(alcohol)
                print(tp.header(['Назваие напитка', 'Инструкиця по приготовлению', 'Ингридиеты'], ))
                print(tp.row([drink, instruction, str(ingredients)], width=10))
                return reqs(req_url)
            else:
                print(alcohol)
                print(tp.header(['Назваие напитка', 'Инструкиця по приготовлению', 'Ингридиеты'], ))
                print(tp.row([drink, instruction, str(ingredients)], width=10))


    reqs(req_url)
# сдесь работаем с ошибмой если нет отсутсвует интернет
except ConnectionError:
    print('Нет соединения с интернетом')
# сдесь работаем со всеми остальными ошибками которые возникают в ходе программы
except Exception as e:
    print('Ошибка:\n', traceback.format_exc())
    print()
