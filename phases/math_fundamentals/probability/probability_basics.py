import math;
import random;

def factorial(n):
    result = 1;
    for i in range(2,n + 1):
        result *= i;
        
    return result;



def combinations(n,k):
    return factorial(n) // (factorial(n) * factorial(n -k));

    
    
def conditional_probability(p_a_and_b, p_b):
    return p_a_and_b / p_b;

def bernoulli_pmf(k,p):
    return p if k == 1 else (1 - p);


def categorical_pmf(k,probs):
    return probs[k];


def poisson_pmf(k,lam):
    return (lam **k) * math.exp(-lam) / factorial(k);

def uniform_pdf(x,a,b):
    if a <= x <=b:
        return 1.0 / (b-a);
    
    return 0.0;

    
def normal_pdf(x,mu,sigma):
    coeff = 1.0 / (sigma * math.sqrt(2 * math.pi))
    exponent = -0.5 * (((x-mu)) / sigma) ** 2;
    return coeff * math.exp(exponent);



def expected_value(values,probabilities):
    return sum(v * p for v,p in zip(values, probabilities))

    
def variance(values, probabilities):
    mu = expected_value(values,probabilities);
    return sum(p*(v - mu)** 2 for v,p in zip(values,probabilities));

    
def sample_bernoulli(p,n=1):
    return [1 if random.random() < p else 0 for _ in range(n)];


def sample_categorical(probs , n =1 ):
    cumulative = [];
    total = 0;
    for p in probs:
        total += p;
        cumulative.append(total);
        
    samples = [];
    for _ in range(n):
        r = random.random();
        for i  ,c in enumerate(cumulative):
            if r <= c:
                samples.append(i);
                break;
    return samples;

    
def sample_normal_box_muller(mu,sigma,n=1):
    samples = [];
    for _ in range(n):
        u1 = random.random();
        u2 = random.random();
        z = math.sqrt(-2 * math.log(u1)) * math.cos(2*math.pi*u2);
        samples.append(mu + sigma * z);
    return samples;

                



p_king_given_face = conditional_probability(4 / 52, 12 / 52);
print(f"P(King | Face card) = {p_king_given_face:.4f}")

die_values = [1, 2, 3, 4, 5, 6]
die_probs = [1/6] * 6
mu = expected_value(die_values, die_probs)
var = variance(die_values, die_probs)
print(f"Die: E[X] = {mu:.4f}, Var(X) = {var:.4f}, SD = {var**0.5:.4f}")