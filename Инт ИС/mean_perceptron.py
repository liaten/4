import random
from statistics import mean # среднее арифметическое чисел в списке

ii = 2
jj = 100
epochas = 10
random.seed(1)

# формируем исходные списки значений чисел по ii в каждом вложенном списке
dataset = [[random.uniform(0,1) for i in range(ii)] for j in range(jj)]
# их среднее арифметическое
dataset_means = [mean(data) for data in dataset]
# обозначаем веса
weights = [random.uniform(0,1) for i in range(ii)]

print(weights)
for iteration in range(epochas): # эпохи
    for j in range(jj): # итерации
        output = weights[0] * dataset[j][0] + weights[1] * dataset[j][1]
        weights = [weights[i] + weights[i] * (dataset_means[j] - output) * dataset[j][i] for i in range(ii)]
        # print(output, weights)

print('mean of 3 and 5 is ', weights[0]*3+weights[1]*5)
print('mean of 2 and 10 is ', weights[0]*2+weights[1]*10)
