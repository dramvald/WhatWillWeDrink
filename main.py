import traceback
import drink
ALCOHOL = 'Alcoholic'
req_url = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
try:
    tipple, instruction, ingredients, measure = drink.interpellation(req_url)
    drink.conclusion(tipple, instruction, ingredients, measure)
except ConnectionError:
    print('Нет соединения с интернетом')
# Здесь работа над всеми остальными ошибками которые возникают в ходе программы.
except Exception as e:
    print('Ошибка:\n', traceback.format_exc())
    print()