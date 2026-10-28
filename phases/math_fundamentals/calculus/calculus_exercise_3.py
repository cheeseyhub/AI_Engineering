import numpy as np
import time

def loss_function_to_minimize(x,h=0):
    left_of_point = (x-h)**4   - (3*(x-h)**2);
    right_of_point = (x+h)**4  - (3*(x+h)**2);
    average_of_point = (right_of_point - left_of_point) / (2*h);
    return average_of_point 
    
    
start_time_with_out_velocity = time.perf_counter();
learning_rate = 0.001;

x =np.array([10,-10],dtype=float);

for epoch in range(70000):
    d_function = loss_function_to_minimize(x,1e-10);
    x = x - (learning_rate* d_function);
    x = np.round(x,decimals=10)

end_time_with_out_velocity = time.perf_counter();


total_time_with_out_velocity  = end_time_with_out_velocity - start_time_with_out_velocity;
    

print(f"The value for which the loss is minimum is {x} ");
print(f"Total time without velocity : {total_time_with_out_velocity}")






start_time_with_velocity = time.perf_counter();


velocity_vector = 0;


new_x = np.array([10,-10],dtype=float);
for epoch in range(70000):
    d_function = ( (4* (new_x**3)) - (6*new_x));
    if d_function[0] < 1e-1 and d_function[1] < 1e-1:
        continue;

    velocity_vector = 0.1* velocity_vector + (learning_rate *d_function)
    

    new_x = new_x - velocity_vector;
    new_x = np.round(new_x,decimals=10)





end_time_with_velocity = time.perf_counter();
total_time_with_velocity  = end_time_with_velocity - start_time_with_velocity;

print(f"The value for which the loss is minimum is {new_x} ");
print(f"Total time with velocity : {total_time_with_velocity}")

