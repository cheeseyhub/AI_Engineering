import numpy as np;

#function to find the derivative of 
def f(x,y):
    return (x-3)**2 + (y+1)**2;



x = np.array([0,1,2,3],dtype=float);
x /= np.max(x);
y = np.array([0,1,2,3],dtype=float);
y /= np.max(y);
z = f(x,y);
z/= np.max(z)



weight1 = np.random.randn();
weight2 = np.random.randn();

learning_rate = 0.01;




for i in range(600):
    predict = (weight1-3)**2 + (weight2 + 1)**2;
    error = predict - z;
    loss = error**2;

    dweight1 = np.mean( 2 * (weight1 - 3) )
    dweight2 = np.mean(2 * (weight2 +1));

    
    weight1 -= learning_rate *dweight1;
    weight2 -= learning_rate *dweight2;

    


print(f" ({weight1:.4f}-3)**2 + ({weight2:.4f}+1)**2; ")




    
