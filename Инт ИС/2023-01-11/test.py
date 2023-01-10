import numpy as np
import random
import matplotlib.pyplot as plt


data_sample = np.array([[130, 94], [51, 74], [640, 147], [28, 58], [80, 86], [110, 94], [33, 63], [90, 86], [36, 69],
            [38, 72], [366, 128], [84, 85], [80, 82], [83, 86], [70, 88], [61, 72], [54, 74], [44, 61],
            [106, 90], [84, 89], [39, 68], [42, 76], [197, 114], [102, 90], [57, 78]],np.uint8)


crocs_types = {} # связанный список: id крокодила - тип крокодила


# Функция нормирования векторов
def normalize(array):
    norm_array = np.zeros_like(array,dtype=np.float32)
    for i in range(len(array)):
        x = array[i][0]
        y = array[i][1]
        length = (x ** 2 + y ** 2) ** 0.5
        x_norm = x / length
        y_norm = y / length
        # Проверка, как в экселе: (раскомментировать, если захочется понять работу нормализации)
        # check = (x_norm**2 + y_norm**2) ** 0.5
        # print(f"x:{x}, y:{y}, len: {length}, x_norm:{x_norm}, y_norm:{y_norm}, check: {check}")
        norm_array[i] = [x_norm,y_norm]
        # print(norm_array[i])
    return norm_array


def study(croc, weights_o, position):
    x1 = croc[0]
    x2 = croc[1]
    lengths = []
    len_weights = len(weights_o)

    # Считаем длины
    lengths = np.array([((weights_o[i][0] ** 2 + weights_o[i][1] ** 2) ** 0.5) for i in range(len_weights)],dtype=np.float32)
    print(f"Lengths: {lengths}")

    # Считаем нормированные веса
    norm_weights = np.array([[(weights_o[i][0] / lengths[i]),(weights_o[i][1] / lengths[i])] for i in range(len_weights)], np.float32)
    print(f"Norm weights: {norm_weights}")

    results = np.zeros(shape=len_weights,dtype=np.float32)
    print(results)
    result_max = 0
    croco_type = 0
    # Считаем результаты, определяем тип крокодила и пересчитываем иксы
    for i in range(len_weights):
        results[i] = x1 * norm_weights[i][0] + x2 * norm_weights[i][1]
        if(results[i]>result_max):
            result_max = results[i]
            croco_type = i
    print(results)

    x1_new = norm_weights[croco_type][0] + 0.5 * (x1 - norm_weights[croco_type][0])
    x2_new = norm_weights[croco_type][1] + 0.5 * (x2 - norm_weights[croco_type][1])
    croc[0] = x1_new
    croc[1] = x2_new
    crocs_types[position] = croco_type
    # print(f"x1: {x1}\nx2: {x2}\nResults: {results}\nR_max: {result_max}\nCroco type: {croco_type+1}\ncrocs types: {crocs_types[position]}\nx1_new:{croc[0]}\nx2_new:{croc[1]}")



def main():
    # Считываем исходные данные: количество перцептронов, минимальный и максимальный вес, количество эпох
    # p_amnt = int(input("Input the amount of perceptrons: ")) # чем больше, тем больше групп будем выявлять
    # weights_min = float(input("Input the minimal weight in range (0,1): "))
    # weights_max = float(input("Input the maximal weight in range (0,1) (more than minimal weight): "))
    # eras = int(input("Input the amount of eras: ")) # С каждой эпохой будем производить кластеризацию по новой
    
    p_amnt = 3
    weights_min = 0.01
    weights_max = 0.1
    eras = 1

    # Генерируем вес для каждого перцептрона
    weights = np.array([[random.uniform(weights_min,weights_max), random.uniform(weights_min,weights_max)] for i in range(p_amnt)],np.float32)
    print(f"Generated weights:\n{weights}")

    norm_data = normalize(data_sample)
    print(norm_data)

    # Исходные данные в графическом виде
    x_graph = np.array([values[0] for values in norm_data],dtype=np.float32)
    y_graph = np.array([values[1] for values in norm_data],dtype=np.float32)
    plt.scatter(x_graph, y_graph)
    plt.show()

    study(croc=norm_data[0],weights_o=weights, position=0)

if __name__ == "__main__":
    main()