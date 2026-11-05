"""
Problem:
Implement inverse transform sampling for the exponential distribution .
Verify by sampling 10,000 values and comparing the histogram to the true PDF.



The pdf which just tells the probability at a point is just
f(x) = lambda * e^(-lambda*x)

And the CDF which tells 
the total probability of the event actually happening is
f(x) = 1 - e^(-lambada * x);


so  its inverse is 

x = -1/lambda  * ln( 1- U);
where lambda is the average rate and U is the point in time



so if the original point told the probability of a event happening
at a certain point

the inverse will tell the point at which the event when given the probability
"""

import math


def inverse_exponential_distribution(average_rate , probability):

    average_inverse = -1 / average_rate;

    return average_inverse * math.log(probability);

    
    
    
print(inverse_exponential_distribution(0.5,0.2));



