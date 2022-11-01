from time import time
import numpy as np

# сравнение 
x = np.linspace(-3, 3, 1000000)
#print(x)
# задаём  функцию
def f(x):    
    return 2 * np.sin(x) + 5
 
start = time()
f = np.vectorize(f)
# вычисляем вектор значений функции

y = f(x)
print("время векторизации:    ", time() - start)
#print(y, type(y))

# 
x = np.linspace(-3, 3, 1000000)
#print(x)
start = time()
y = 2 * np.sin(x) + 5
print("время векторной операции:    ", time() - start)
#print(y, type(y))


print('='*20)
