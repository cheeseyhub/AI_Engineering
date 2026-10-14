import math;

# Dual number: (value, derivative)
# (2, 1) means: value is 2, derivative w.r.t. x is 1

# Arithmetic rules:
# (a, a') + (b, b') = (a+b, a'+b')
# (a, a') * (b, b') = (a*b, a'*b + a*b')
# sin(a, a')         = (sin(a), cos(a)*a')



class Value:
    def __init__(self,data,gradient = 1):
       self.data = data;
       self.gradient = gradient;
       
    def __add__(self, other):
        other = other if isinstance(other,Value) else Value(other);
        result = Value(self.data + other.data, self.gradient + other.gradient);
        return result;

    def __radd__(self, other):
        other = other if isinstance(other,Value) else Value(other);
        return Value(other) + self;


        
    def __neg__(self):
        other = other if isinstance(other,Value) else Value(other);
        return Value(self.data * - 1 , self.gradient*-1);

        
    def _sub__(self, other):
        other = other if isinstance(other,Value) else Value(other);
        result.data   = self.data +  (-other.data);
        result.gradient = self.data + (-other.gradient);
        return result;

        
    def __mul__(self, other):
        other = other if isinstance(other,Value) else Value(other);
        result = Value(self.data * other.data)
        result.gradient = (self.gradient*other.data) + (self.data*other.gradient); 
        return result;

    def sin(self):
        return  Value(math.sin(self.data), math.cos(self.data)) 


    def __pow__(self, other):
        result = Value(self.data,(other)*((self.data)**(other-1)));
        return result; 
        
        


        



#(5,10)  + (5,15)
def expr(x):
    return Value(x)**2 +  Value(x)*3


# y = x ** 2 + 3 *x 
result = expr(5) ;


print(f"Using dual numbers the gradient is : {result.data} , {result.gradient}");



        
        
        
    
