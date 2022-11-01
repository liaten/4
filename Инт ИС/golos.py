# на вход подаются 5 значений (при >=3 единичек возвращает 1),
# научить программу считать при помощи keras
from itertools import product
import numpy as np

dataset = []
for data in list(product([0,1],repeat=5)):
    if(sum(data)>2):
        data = data + (1,)
    else:
        data = data + (0,)
    dataset.append(data)
arr_dataset = np.array(dataset)
print(arr_dataset)