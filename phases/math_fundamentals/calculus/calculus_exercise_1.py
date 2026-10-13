import numpy as np

def numerical_derivative(f,x, h=1e-7):
    return (f(x+ h) - f(x-h)) / (2*h);

def numerical_derivative_2nd(f,x,h=1e-7):
    first_derivative = lambda val: numerical_derivative(f,val,h);
    return numerical_derivative(first_derivative,x,h)


def numerical_derivative_3rd(f,x,h=1e-2):
    second_derivative = lambda val: numerical_derivative_2nd(f,val,h);
    return numerical_derivative(second_derivative,x,h)

# x^3 -> 3x^2
# 3x^2 -> 6x
# 6x -> 6


# f(x)' = (f(x+ h) - f(x) / h)

# 1/h  (f(x+h)'*x - f(x)')

# f(x+h) = > f(x+2h)  -f(x+h ) / h



# 1 / h (f(x+2h) - f(x+h)/h - (fx+h) +f(x) /h )


# f(x+2h) -f(x+h) -f(x+h) +f(x) / h^2;
# f(x+2h) -2f(x+h) +f(x) / h^2

def cube(x):return x**3;

first_derivative = numerical_derivative(cube,2);
print(f"First derivative : {first_derivative:.4f}");

second_derivative = numerical_derivative_2nd(cube,2);

print(f"Second  derivative : {second_derivative:.4f}");


third_derivative = numerical_derivative_3rd(cube,2);
print(f"Third derivative : {third_derivative:.4f}")
    