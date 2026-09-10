import numpy as np

def function_to_predict(input):
    return input * input ;

x = np.array([1,2,3,4,5,6,7,8,9],dtype=float);
y = np.array([ function_to_predict(i) for i in x],dtype=float);




#weight1*x^2 + weight2*x  +   bias

weight1 = np.random.randn();
weight2 = np.random.randn();
bias = np.random.randn();
learning_rate = 0.0001



# 

for epoch in range(5000):
    prediction = (weight1 * x *x) + (weight2 * x) + bias;
    error = prediction - y;
    loss = np.mean(error ** 2);

    dw1 = np.mean(2 * error * x * x);
    dw2 = np.mean(2*error * x);

    db = np.mean(2 * error);

    
    weight1 -= learning_rate * dw1;
    weight2 -= learning_rate * dw2;
    bias -= learning_rate * db

    
print(f"{weight1}x^2 + {weight2}x + {bias}");




