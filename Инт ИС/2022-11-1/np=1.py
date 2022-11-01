from time import time
import numpy as np

# сравнение матричной операции и поэлементных в цикле
l = np.array(range(1000000), dtype=np.uint64)
start = time()
l += 1
print("время с np:    ", time() - start)

l = list(range(1000000))
start = time()
for i in range(len(l)):
    l[i] += 1
print("время без np: ", time() - start)
print('='*20)

# матричная проверка условия и поэлементная проверка в цикле
a = np.random.rand(200, 1000) # двумерный массив нулей
#print(a)
z = np.zeros((200,1000)) # двумерный массив нулей
start = time()
z = np.where(a > 0.5, a, a+1)
print("время с np:    ", time() - start)
#print(z)

a = np.random.rand(200, 1000)
z = np.zeros((200,1000)) 
start = time()
for i in range(200):
    for j in range(1000):
        if a[i,j]>0:
            z[i,j]=a[i,j]
        else:
            z[i,j]+=1
print("время без np:    ", time() - start)
print('='*20)

# использование в качестве итератора np.arange и range
k=0
start = time()
for i in np.arange(1, 1000000, 1, dtype=int):
    k+=1
print("время с np:    ", time() - start)

k=0
start = time()
for i in range(1, 1000000):
    k+=1
print("время без np:    ", time() - start)









