import math
from collections import defaultdict
"""
p(B) = p(B | A) * P(A) + P(B | not A ) * p(not A)

p(A | B) = Posterior Your updated belief about A after seeing evidence B
p(B | A) = How porbable the evidence B is if A is true
p(A)  = Prior Your belief about A before seeing any evidence.
p(b) = Evidence Total probability of seeing B under all the possibilities.



"""

def bayes(prior, likelihood, false_positive_rate):
    evidence = likelihood * prior + false_positive_rate * (1- prior);
    posterior = likelihood * prior / evidence;
    return posterior;

    
result = bayes(prior=0.0001, likelihood=0.99, false_positive_rate=0.01)
print(f"P(sick|positive) = {result:.4f}")


"""
Todo: Build a naive Bayer classifier which is used in spam filtering  and recommendation systems.

"""




