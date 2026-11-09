"""

Build a joint distribution table for two loaded dice. Compute the marginal distributions and check whether the dice are independent.



From what i know i need to build a table for one loaded die lets say x 
and then one for  a die named y.
"""
import random
import math

# Table 1 for loaded dice 1;

x = [random.random() for _ in range(6)];
x = [element  / sum(x) for element in x];

# Table 2 for loaded dice 2;

y = [random.random() for _ in range(6)];
y = [element  / sum(y) for element in y];




## Making the marignal table by multiplying the probabilities
grid = [ [ x[i] * y[j] for i in range(len(x)) ] for j in range(len(y)) ]


## summing the row to find the actual  value


## Matching the row sum
for i in range(len(grid)):
    rowSum = 0;
    for j in range(len(grid[0])):
        rowSum +=grid[i][j];
        
        
    print(rowSum);
    print(y[i]);
    print(math.isclose(rowSum,y[i]));

        

## Matching the column sum

for i in range(len(grid)):
    columnSum = 0;
    for j in range(len(grid[0])):
        columnSum +=grid[j][i];

    print(columnSum);
    print(x[i]);
    print(math.isclose(columnSum,x[i]));



    
