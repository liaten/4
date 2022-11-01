import matplotlib.pyplot as plt
import numpy as np

# 
x = np.linspace(-1, 1, 100).reshape(-1, 1)
#print(x)

# вычисляем вектор значений функции
y = 3 * x + 4
#print(y)

# создаём модель нейросети, используя Keras
from keras.models import Sequential
from keras.layers import Dense
def baseline_model():
    model = Sequential()
    model.add(Dense(1, input_dim=1, activation='linear'))
    model.compile(loss='mean_squared_error', optimizer='sgd')
    return model
# тренируем сеть
model = baseline_model()
model.fit(x, y, epochs=10, verbose = 0)

# отрисовываем результат приближения нейросетью поверх исходной функции
plt.scatter(x, y, color='black', antialiased=True)
print('ups')
plt.plot(x, model.predict(x), color='magenta', linewidth=2, antialiased=True)
plt.show()

# выводим веса на экран
for layer in model.layers:
    weights = layer.get_weights()
    print(weights)



























