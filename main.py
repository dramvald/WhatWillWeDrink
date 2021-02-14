import traceback
import drink
import requests

RANDOM_DRINK_API_URL = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
INGREDIENT = 'strIngredient'
MEASURE = 'strMeasure'

try:
    drinks, instruction, data_drinks = drink.get_drink_data(RANDOM_DRINK_API_URL)
    ingredients = drink.sort_values(data_drinks, INGREDIENT)
    measure = drink.sort_values(data_drinks, MEASURE)
    drink.show_drink(drinks, instruction, ingredients, measure)
# Здесь работа над ошибкой, когда отсутствует интернет.
except ConnectionError:
    print('No internet connection!')
except requests.ConnectionError:
    print('No internet connection!')

# Здесь работа над всеми остальными ошибками которые возникают в ходе программы.
except Exception as e:
    print('Error:\n', traceback.format_exc())
    print()
