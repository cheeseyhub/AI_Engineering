import torch
class Value:
    def __init__(self,data, children=(), op=''):
        self.data = data;
        self.grad = 0.0;
        self._backward = lambda : None 
        self._prev = set(children)
        self._op = op 

    def __repr__(self):
        return f"Value(data={self.data:.4f}, grad={self.grad:.4f})";


# This creates the point 2.0 at which the gradient will be calculated.
x = torch.tensor(2.0,requires_grad=True);
y = x ** 2 + 3 *x + 1;

# Doing back propogation on the function
y.backward();
print(x.grad)