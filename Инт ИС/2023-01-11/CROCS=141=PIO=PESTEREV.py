from matplotlib.colors import ListedColormap
from matplotlib.pyplot import scatter, show, colorbar
from numpy import arange
from random import uniform,choice


# Исходный массив данных крокодилов
data_sample = [[130, 94], [51, 74], [640, 147], [28, 58], [80, 86], [110, 94], [33, 63], [90, 86], [36, 69],
            [38, 72], [366, 128], [84, 85], [80, 82], [83, 86], [70, 88], [61, 72], [54, 74], [44, 61],
            [106, 90], [84, 89], [39, 68], [42, 76], [197, 114], [102, 90], [57, 78]]


crocs_types = {} # связанный список: id крокодила - тип крокодила


# Функция нормирования векторов
def normalize(array):
    norm_array = []
    for i in range(len(array)):
        x = array[i][0]
        y = array[i][1]
        length = (x ** 2 + y ** 2) ** 0.5
        x_norm = x / length
        y_norm = y / length
        # Проверка, как в экселе: (раскомментировать, если захочется понять работу нормализации)
        # check = (x_norm**2 + y_norm**2) ** 0.5
        # print(f"x:{x}, y:{y}, len: {length}, x_norm:{x_norm}, y_norm:{y_norm}, check: {check}")
        norm_array.append([x_norm,y_norm])
    return norm_array
    

def study(croc, weights_o, position):
    x1 = croc[0]
    x2 = croc[1]
    lengths = []
    len_weights = len(weights_o)
    # Считаем длины
    for i in range(len_weights):
        w1 = weights_o[i][0]
        w2 = weights_o[i][1]
        l = (w1 ** 2 + w2 ** 2) ** 0.5
        lengths.append(l)
    # print(f"Lengths: {lengths}")
    # Считаем нормированные веса
    norm_weights = []
    for i in range(len_weights):
        w1 = weights_o[i][0] / lengths[i]
        w2 = weights_o[i][1] / lengths[i]
        norm_weights.append([w1,w2])
    # print(f"Norm weights: {norm_weights}")
    results = []
    r_max = 0
    croco_type = 0
    # Считаем результаты, определяем тип крокодила и пересчитываем иксы
    for i in range(len_weights):
        r = x1 * norm_weights[i][0] + x2 * norm_weights[i][1]
        if(r>r_max):
            r_max = r
            croco_type = i
        results.append(r)
    x1_new = norm_weights[croco_type][0] + 0.5 * (x1 - norm_weights[croco_type][0])
    x2_new = norm_weights[croco_type][1] + 0.5 * (x2 - norm_weights[croco_type][1])
    croc[0] = x1_new
    croc[1] = x2_new
    crocs_types[position] = croco_type
    # print(f"x1: {x1}\nx2: {x2}\nResults: {results}\nR_max: {r_max}\nCroco type: {croco_type+1}\ncrocs types: {crocs_types[position]}\nx1_new:{croc[0]}\nx2_new:{croc[1]}")


def main():
    # Считываем исходные данные: количество перцептронов, минимальный и максимальный вес, количество эпох
    p_amnt = int(input("Input the amount of perceptrons: ")) # чем больше, тем больше групп будем выявлять
    weights_min = float(input("Input the minimal weight in range (0,1): "))
    weights_max = float(input("Input the maximal weight in range (0,1) (more than minimal weight): "))
    eras = int(input("Input the amount of eras: ")) # С каждой эпохой будем производить кластеризацию по новой

    # Генерируем вес для каждого перцептрона
    weights = [[uniform(weights_min,weights_max), uniform(weights_min,weights_max)] for i in range(p_amnt)]
    print(f"Generated weights:\n{weights}")

    # Нормализуем исходные данные
    norm_data = normalize(data_sample)
    print(f"Normalized data:\n{norm_data}")

    # Исходные данные в графическом виде
    x_graph = [values[0] for values in norm_data]
    y_graph = [values[1] for values in norm_data]
    scatter(x_graph, y_graph)
    show()
    
    for era in range(eras):
        clustered_data = [] # данные о крокодилах, но в массиве

        for i in range(len(norm_data)):
            study(croc=norm_data[i],weights_o=weights, position=i)

        clustered_data = []
        for i in crocs_types:
            clustered_data.append(crocs_types[i])

    print(f"New normalized data:\n{norm_data}")
    print(f"List of croco types: {clustered_data}")
    
    # Генерируем рандомные цвета для вывода по классам
    colors = ["#"+''.join([choice('0123456789ABCDEF') for j in range(6)])
            for i in range(p_amnt)]
    print(f"List of colors:{colors}")

    for i in range(len(norm_data)):
        scatter(x_graph, y_graph, c=clustered_data, cmap=ListedColormap(colors))
    cb = colorbar()
    loc = arange(0, max(clustered_data), max(clustered_data) / float(len(colors)))
    cb.set_ticks(loc)
    cb.set_ticklabels(colors)
    show()


if __name__ == "__main__":
    main()