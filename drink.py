import requests
import json
import traceback
from prettytable import PrettyTable
p = PrettyTable()

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
            measure = item['strMeasure1'], item['strMeasure2'], item['strMeasure3'], \
                      item['strMeasure4'], item['strMeasure5'], item['strMeasure6'], \
                      item['strMeasure7'], item['strMeasure8'], item['strMeasure9'], \
                      item['strMeasure10'], item['strMeasure11'], item['strMeasure12'], \
                      item['strMeasure13'], item['strMeasure14'], item['strMeasure15']
            # уменьшаю список убирая в ingredients и measure элементы имеющие None
            ingredients = list(filter(None, ingredients))
            measure = list(filter(None, measure))
            # делаю проверку на алкогольный или без алкогольный напиток, и если он без алкогольный,
            # то отправляеться сново запрос и проходит по циклу
            if alcohol != 'Alcoholic':
                return reqs(req_url)
            else:
                print(alcohol)
                p.add_column('Drink name', [drink])
                p.add_column('Instructions for preparation', [instruction])
                p.add_column('Ingredients', [ingredients])
                p.add_column('Ingredient quantity', [measure])
                print(p.get_string())


    reqs(req_url)
    input()
# здесь работа над ошибмой, когда отсутсвует интернет
except ConnectionError:
    print('Нет соединения с интернетом')
# здесь работа над всеми остальными ошибками которые возникают в ходе программы
except Exception as e:
    print('Ошибка:\n', traceback.format_exc())
    print()
