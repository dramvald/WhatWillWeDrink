import traceback
import drink
import requests

ALCOHOL = 'Alcoholic'
# req_url адрес сервера
req_url = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
try:
    tipple, instruction, ingredients, measure = drink.interpellation(req_url)
    drink.conclusion(tipple, instruction, ingredients, measure)
# Здесь работа над ошибкой, когда отсутствует интернет.
except ConnectionError:
    print('No internet connection!')
except requests.ConnectionError:
    print('No internet connection!')

# Здесь работа над всеми остальными ошибками которые возникают в ходе программы.
except Exception as e:
    print('Error:\n', traceback.format_exc())
    print()
