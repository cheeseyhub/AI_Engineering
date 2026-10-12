import random
from mini_mlp import MLP


# A multi-layer precptron 
# with 2 inputs 4 hidden layer neurons and 1 output

model = MLP([2,4,1]);


xs = [[0,0],[0,1],[1,0],[1,1]];
ys = [-1,1,1,-1];



for step in range(1000):
    preds = [model(x) for x in xs];

    loss = sum((p - y) ** 2 for p, y in zip(preds, ys))


    for p in model.parameters():
        p.grad = 0.0
    loss.backward();

    lr  = 0.5
    for p in model.parameters():
        p.data -=  lr * p.grad;

    if step %20 ==0:
        print(f"step {step:3d}  loss = {loss.data:.4f}")

        
print("\nPredictions after training:")
for x, y in zip(xs, ys):
    print(f"  input={x}  target={y:2d}  pred={model(x).data:6.3f}")
