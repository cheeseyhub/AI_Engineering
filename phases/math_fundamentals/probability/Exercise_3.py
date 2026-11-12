"""

compute the cross-entropy loss for a 
5-class classifier that outputs logits 
[2.0, 0.5, -1.0, 3.0, 0.1]
when the correct class is index 3.
then verify your answer with pytorch's nn.crossentropyloss.

"""

import math;

def soft_max(inputs):
    total = sum([math.exp(x) for x in inputs]);
    return [(math.exp(x) / total) for x in inputs];


x = [2.0,0.5,-1.0,3.0,0.1];
# activating the logits with softmax
y = soft_max(x);

loss = -math.log(y[3]);

print(f"Manual Loss : {loss:.6f}");

# comparing with the torch loss
import torch
import torch.nn as nn

tensor = torch.tensor([x]);
target = torch.tensor([3]);

loss_fn = nn.CrossEntropyLoss();


result = loss_fn(tensor,target);
print(f"Pytorch Loss : { result.item():.6f}");

