from Matrix import Matrix
import numpy as np

def relu_matrix(m):
    return Matrix([[max(0,val) for val in row] for row in m.rows])

    
    

input = Matrix([
    [np.random.rand()]
    for _ in range(3)
]);

# layer_1
# W @ input ( 4 * 3) ( 3 * 1) + bias;
# -> multiplication produces a 4 x 1     
layer_1_weights = Matrix([
    [np.random.rand() for _ in range(3)]  
    for _ in range(4)
])
layer_1_bias = Matrix([
    [np.random.rand()]
    for _ in range(4)
]) 



layer_1_result = (layer_1_weights @ input) + layer_1_bias

layer_1_result = relu_matrix(layer_1_result);


# output  2 * 1
# (2 * 4) ( 4 * 1) + bias


layer_2_weights = Matrix([
    [np.random.rand() for _ in range(4)]
    for _ in range(2)
])

layer_2_bias = Matrix([
    [np.random.rand() ]
    for _ in range(2)
])

output = (layer_2_weights @ layer_1_result) + layer_2_bias



print(output)








