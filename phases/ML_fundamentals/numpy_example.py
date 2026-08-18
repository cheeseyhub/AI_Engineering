import numpy as np;

a = np.array([1,2,3],dtype=float);
b = np.array([4,5,6],dtype=float);


print(f"a + b = {a + b }")
print(f" a . b =  {np.dot(a,b)}");
print(f"|a| = {np.linalg.norm(a):.4f}");


# a.b = |a||b| costheta;
# costheta = a.b/ |a||b|


print(f"cosime similarity = {np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b)):.4f}")


W = np.random.randn(2,3) * 0.1;
X = np.array([1.0,0.5,-0.3])

print(f"Wx = { W @ X}");

