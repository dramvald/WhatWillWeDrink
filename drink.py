import requests
import json
import tableprint as tp
import traceback

try:
    # Делам запрос на сервер по адресу req_url и выводим результат.
    req_url = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
    resp = requests.get(req_url).text
    print(resp)

    print(type(resp))  # Тип данных которые мы запросили
    print('___________')
    # Преобразуем строку json в обьект python типа dict.
    date = json.loads(resp)
    print(type(date))
    print(date['drinks'])  # вывожу содержимое ключа drinks
    # Так как содержимае ключа drinks имеет тип list,
    # использую for для того чтобы пройтись по элементам списка,
    # которые являються словорями, и взять нужные данные.
    for item in date["drinks"]:
        drink = item['strDrink']
        instruction = item['strInstructions']
        ingredients = item['strIngredient1'], item['strIngredient2'], item['strIngredient3'], \
                      item['strIngredient4'], item['strIngredient5'], item['strIngredient6'], \
                      item['strIngredient7'], item['strIngredient8'], item['strIngredient9'], \
                      item['strIngredient10'], item['strIngredient11'], item['strIngredient12'], \
                      item['strIngredient13'], item['strIngredient14'], item['strIngredient15']
        print('Название напитка: ' + drink)
        print('Интсрукция: ' + instruction)
        print('Ингридиенты: ' + str(ingredients))

        print(tp.header(['Назваие напитка', 'Инструкиця по приготовлению', 'Ингридиеты']))

        print(tp.row([drink, instruction, str(ingredients)]))
        #print(tp.table())
except ConnectionError:
    print('Нет соединения с интернетом')
except Exception as e:
    print('Ошибка:\n', traceback.format_exc())
    print()
