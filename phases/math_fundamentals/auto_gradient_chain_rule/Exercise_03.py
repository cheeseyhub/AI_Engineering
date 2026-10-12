import torch

#                   f 
#               |       \ 
#               t       b
#           /        \  
#          |          |
#          a          b
# y = relu(w1 * x1 + w2x2 + b);


x1 = torch.tensor(2.0,requires_grad=True);
x2 = torch.tensor(3.0,requires_grad=True);

w1 = torch.randn(());
w2 = torch.randn(());

bias = torch.randn(());



f = (w1*x1 + w2*x2 + bias).relu();

f.backward();






print(f"The gradient of dy/dx1 = {x1.grad}")
print(f"The gradient of dy/dx2 = {x2.grad}")





