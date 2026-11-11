"""

Compute the cross-entropy loss for a 
5-class classifier that outputs logits 
[2.0, 0.5, -1.0, 3.0, 0.1]
when the correct class is index 3.
Then verify your answer with PyTorch's nn.CrossEntropyLoss.

"""

import math;

x = [2.0,0.5,-1.0,3.0,0.1];

outputs = [math.tanh(i) for i in x];
print(outputs);