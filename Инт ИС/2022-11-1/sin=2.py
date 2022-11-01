import matplotlib.pyplot as plt
import numpy as np

# генерируем однородную линейную последовательность - старт, финиш, количество
x = np.linspace(-3, 3, 100, endpoint=False).reshape(-1, 1)
# print(x)
# вычисляем вектор значений функции
y = 2 * np.sin(x) + 5

# создаём модель нейросети, используя Keras
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
def baseline_model():
    model = Sequential()
    model.add(Dense(5, input_dim=1, activation='linear'))
    # model.add(Dense(5, input_dim=1, activation='relu'))
    # ReLU (выпрямитель, f(x) = max(0, x))
    model.add(Dense(1, input_dim=5, activation='linear'))
    
    model.compile(loss='mean_squared_error', optimizer='sgd')
    return model
# тренируем сеть
model = baseline_model()
model.fit(x, y, epochs=40, verbose = 0)

# отрисовываем результат приближения нейросетью поверх исходной функции
plt.scatter(x, y, color='black', antialiased=True)
plt.plot(x, model.predict(x), color='magenta', linewidth=2, antialiased=True)
plt.show()
print('ups')
# выводим веса на экран
for layer in model.layers:
    weights = layer.get_weights()
    print(weights)



























