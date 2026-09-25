import torch
# This creates the point 2.0 at which the gradient will be calculated.
x = torch.tensor(2.0,requires_grad=True);
y = x ** 2 + 3 *x + 1;

# Doing back propogation on the function
y.backward();
print(x.grad)
