import numpy as np
from scipy import stats

normal = stats.norm(loc=0, scale=1);
samples = normal.rvs(size=1000)

# print(f"Mean : {np.mean(samples):.4f}, Std: {np.std(samples):.4f}");
# print(f"P(X < 1.96) = {normal.cdf(1.96):.4f}");

logits = np.array([2.0,1.0,0.1]);
from scipy.special import softmax,log_softmax
probs = softmax(logits);
log_probs = log_softmax(logits)

print(f"Softmax : {probs}");
print(f"Log-softmax : {log_probs}");