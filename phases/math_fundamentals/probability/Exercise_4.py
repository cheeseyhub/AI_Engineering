"""

Write a function that takes a list of log probabilities and 
returns the most likely sequence,
the total log probability,
and the equivalent raw probability.
Test it with a sentence of 50 words where each word has probability 0.01.


"""
import math;
import random

def raw_to_log_conversion(raw_probabilities):
    return [math.log(x) for x in raw_probabilities];

def most_likely_log_probability(log_probabilities):
    return max(log_probabilities);

def total_log_probability(log_probabilities):
    return sum(log_probabilities);

def equivalent_raw_probabilities(log_probabilities):
    return [math.exp(x) for x in log_probabilities];

    
# In actuality  each word is suppose to multiply meaning 0.01 * 0.01 and so 
# but according to rule of logirithim multiplication becomes addition
# so thus we do log(0.01) + log(0.01) and so on.
# so we sum the "log probabilities"

def sentence_log_probability(sentence):
        
    total = total_log_probability(raw_to_log_conversion(sentence));
    return total;

    

# In raw probability we actually multiply stuff.
def sentence_raw_probability(sentence):
    raw_total = math.exp(sentence_log_probability(sentence));
    return raw_total;

    
def single_function_for_exercise(log_probabilities):
   maximum =  most_likely_log_probability(log_probabilities)
   total = total_log_probability(log_probabilities);
   raw = equivalent_raw_probabilities(log_probabilities);

   return (maximum, total , sentence_raw_probability(raw)) ;

    
# Using sentence split into an array;

sentence = "As the brave young astronaut floated silently outside the silver spacecraft, she gazed down at the glowing blue curvature of Earth, realizing how vast and fragile our home truly is while drifting weightlessly through the endless darkness of outer space filled with millions of shimmering distant stars and bright galaxies.";
sentence_probability = [0.01] * 50;
probabilities = raw_to_log_conversion(sentence_probability) ;

print(f"maximum Log : {single_function_for_exercise(probabilities)[0]}")
print(f"total Log : {single_function_for_exercise(probabilities)[1]}")
print(f"Raw Log : {single_function_for_exercise(probabilities)[2]}")


    
    



