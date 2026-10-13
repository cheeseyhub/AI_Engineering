

# Dual number: (value, derivative)

# (2, 1) means: value is 2, derivative w.r.t. x is 1

# Arithmetic rules:
# (a, a') + (b, b') = (a+b, a'+b')
# (a, a') * (b, b') = (a*b, a'*b + a*b')
# sin(a, a')         = (sin(a), cos(a)*a')



class Value:
    def __init__(self,data,gradient):
       self.data = data;
       self.gradient = gradient;
       
    def __add__(self, other):
        self.data  += other.data;
        self.gradient += other.gradient;
        
    def __neg__(self):
        self.data *= -1;
        self.gradient *=-1;
        
    def _sub__(self, other):
        self.data   = self.data +  (-other.data);
        self.gradient = self.data + (-other.gradient);

        
    def __mul__(self, other):
        self.data = self.data * other.data;
        self.gradient = self.gradient * other.data + self.data* other.gradient; 