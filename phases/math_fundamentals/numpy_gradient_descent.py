import numpy as np;
x = np.array([1,2,3,4,5],dtype=float);
y = np.array([3.0, 5.0, 7.0, 9.0, 11.0],dtype=float)

# predicting the function 2x + 1;

w,b = np.random.randn(), np.random.randn();
lr = 0.01

for epoch in range(2000):
    pred = w*x + b;
    error = pred - y;
    loss = np.mean(error**2);
    dw = np.mean(2 * error * x);
    db = np.mean(2 * error);

    w -= lr * dw;
    b -= lr * db;

    

print(f"Learned : y = {w:.2f}x + {b:.2f}");