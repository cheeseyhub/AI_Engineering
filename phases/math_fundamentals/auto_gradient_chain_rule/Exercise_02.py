from gradient_engine import Value;


x = Value(0);
y = x.tanh();
y.backward();



t = Value(2);
l = t.tanh();
l.backward();


print(f"Gradient of tanh(x) at x = 0 : {x.grad}");
print(f"Gradient of tanh(t) at t = 2 : {t.grad}");