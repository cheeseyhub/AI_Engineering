import numpy as np


rng = np.random.default_rng();

def function_to_predict(input):
    return input**3;

    
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12] ,dtype=float);
x /=  np.max(x)

y = function_to_predict(x);
y /= np.max(y)


# w1x^3 + w2x^2 + w3x + bias

w1 = rng.random()
w2 = rng.random()
w3 = rng.random()
bias = rng.random()




lr = 0.1
for i in range(20000):
    prediction = (w1* (x**3) ) + (w2* (x**2)) + (w3*x) + bias;
    error = prediction - y
    loss = error**2;


    dw1 = np.mean(2* error * (x*x*x))
    dw2 = np.mean(2*error * (x*x))
    dw3 = np.mean(2*error * (x))
    dbias = np.mean(2*error);

    
    
    w1 = w1 - (lr * dw1) ;
    w2 = w2 - (lr * dw2) ;
    w3 = w3 - (lr * dw3) ;
    bias = bias - (lr * dbias) ;



print(f"{w1:.4f} x^3 + {w2:.4f} x^2 + {w3:.4f} x + {bias:.4f}");


