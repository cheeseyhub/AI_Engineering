import numpy as np;

#function to find the derivative of 
def f(x,y):
    return (x-3)**2 + (y+1)**2;

learning_rate = 0.01;


point1 = 0
point2 = 0;


for i in range(2000):
    dx = 2*(point1-3);
    dy = 2*(point2+1);
    point1 =point1 - learning_rate * dx;
    point2 = point2 - learning_rate * dy;

    
print(f"({point1:.4f},{point2:.4f})")
    






    
