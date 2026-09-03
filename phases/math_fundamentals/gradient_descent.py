# https://www.gironi.it/blog/en/the-gradient-descent-algorithm-explained-simply/
# Example form the website above;

# Example 1
import numpy as np
import matplotlib.pyplot as plt



# # Cost function: predicting the price of a house
# area = np.array([50, 70, 90, 120, 150])
# price = np.array([150, 200, 260, 340, 400])  # thousands of euros




# # Model : price  = m * area;

# # MSE Cost  as m varies

# m_values = np.linspace(1,4,301);
# mse = np.array([np.mean((price - m* area)**2) for m in m_values])



# plt.plot(m_values, mse, lw=2, color="steelblue")
# plt.xlabel("m (slope)")
# plt.ylabel("MSE")
# plt.title("Cost function as m varies")
# m_best = m_values[np.argmin(mse)]
# plt.axvline(m_best, color="red", linestyle="--")
# plt.show()
# print(f"The value of m that minimizes the error: {m_best:.2f}")



# Example 2

# f = lambda x : x**2;
# grad_f = lambda x: 2*x;


# x = 10.0;
# alpha = 0.3; # Learning rate
# n_iteration = 50;

# path = np.zeros(n_iteration);


# for i in range(n_iteration):
#     path[i] = x;
#     x = x - alpha * grad_f(x);

    
# print(f"starting point : 10");
# print(f"After 50 iterations x = {x : .8f}");

# print(f"Function value : {f(x)}:.10f");




# # Visualization
# xs = np.linspace(-11, 11, 200)
# plt.plot(xs, xs**2, lw=2, color="steelblue")
# plt.plot(path, path**2, "ro--", markersize=4)
# plt.title("Gradient descent on f(x) = x\u00b2")
# plt.xlabel("x")
# plt.ylabel("f(x)")
# plt.show()


# Example 3 :

def gradient_descent (x0, alpha , n_iter = 30):
    x = x0;
    path = np.zeros(n_iter);
    for i in range(n_iter):
        path[i] = x
        x = x - (alpha *  (2 * x))
    return path;

    

x0 = 8.0;
slow = gradient_descent(x0,alpha=0.01);
right = gradient_descent(x0,alpha=0.1);
fast = gradient_descent(x0,alpha=0.9)



fig, axes = plt.subplots(1, 3, figsize=(14, 4))
xs = np.linspace(-10, 10, 200)
for ax, data, color, title in zip(axes,
        [slow, right, fast],
        ["red", "darkgreen", "orange"],
        ["\u03b1 = 0.01 (too slow)", "\u03b1 = 0.1 (good compromise)",
         "\u03b1 = 0.9 (nearly unstable)"]):
    ax.plot(xs, xs**2, lw=2, color="steelblue")
    ax.plot(data, data**2, "o--", color=color, markersize=4)
    ax.set_title(title)
plt.tight_layout()
plt.show()