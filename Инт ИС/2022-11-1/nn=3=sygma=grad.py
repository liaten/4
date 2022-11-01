from time import time
import numpy as np
np.random.seed(1000)

input_set  = np.random.rand(3000)
#print('x',input_set, input_set.shape)
target_set = np.multiply(input_set, input_set)
#print('y',target_set, target_set.shape)
weights_01 = np.random.rand(1,5)
#print('w01',weights_01)
weights_12 = np.random.rand(1,5)
#print('w12',weights_12)
for iteration in range(15): # это эпохи
    for i in range(3000): # это итерации, каждая итерация содержит 1 экземпляр
        hidden_in = input_set[i]*weights_01
        hidden_out = 1/(1+np.exp(0-hidden_in))
        output_in = np.sum(np.multiply(hidden_out, weights_12))
        output_out = 1/(1+np.exp(0-output_in))
        #print(i,hidden_out,f"{output_out:10.6f}")
        
        error_12 = target_set[i] - output_out # число
        error_01 = error_12 * weights_12  # вектор
        #print("error_12", error_12)
        #print("error_01", error_01, error_01.shape)
        weights_12 += 0.1*hidden_out*error_12*output_out*(1-output_out)
        #print('w12',weights_12)
        weights_01 += 0.1*input_set[i]*error_01*hidden_out*(1-hidden_out)
        #print('w01',weights_01)
    #print(output,weights)        
#
hidden_in = 0.5*weights_01
hidden_out = 1/(1+np.exp(0-hidden_in))
output_in = np.sum(np.multiply(hidden_out, weights_12))
output_out = 1/(1+np.exp(0-output_in))
print('ups',output_out)
