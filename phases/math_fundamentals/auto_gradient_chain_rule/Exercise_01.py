from gradient_engine import Value

x = Value(2);
y = x**3;
y.backward();


print(f"Gradient of x**3 at x = 2 : {x.grad}");