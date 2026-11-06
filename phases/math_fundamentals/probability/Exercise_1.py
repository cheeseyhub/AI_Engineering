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
import random
import matplotlib.pyplot as plt;


def inverse_exponential_distribution(average_rate , probability ):

    average_inverse = -1 / average_rate;

    return average_inverse * math.log(probability);



lambda_param = 0.02
data = [inverse_exponential_distribution(lambda_param, 1.0 - random.random()) for _ in range(10000)]

plt.hist(data, bins=50, density=True, alpha=0.6, color='skyblue', label='Sampled Histogram')

max_val = max(data)
x_pdf = [i * (max_val / 200) for i in range(2001)]
y_pdf = [lambda_param * math.exp(-lambda_param * x) for x in x_pdf]
plt.plot(x_pdf, y_pdf, color='red', linewidth=2, label='True PDF')

plt.legend()
plt.show()
