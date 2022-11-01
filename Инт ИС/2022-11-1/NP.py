import numpy as np
from random import randint
z = np.zeros((4,5),dtype=np.int32) # двумерный массив нулей
print('z',z.shape)
o = np.ones(10) # одномерный массив единиц
print(o)
f = np.full((4,3,2), 7.5, dtype = np.int8) # 
print('f',f.shape)
print(f)
a = np.arange(10,30) #
print(a)
a = a[::-1] #
print(a)
nz = np.nonzero([1,2,0,0,4,0]) # индексы ненулевых элементов
print(nz)
oo = np.eye(3) # единичная матрица
print(oo)













