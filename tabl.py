import tableprint as tp
import numpy as np

date = np.random.randn(10, 3)
headers = ['Назваие напитка', 'Инструкиця по приготовлению', 'Ингридиеты']

tp.table(date, headers)
print(tp.header(['A', 'B', 'C']))


