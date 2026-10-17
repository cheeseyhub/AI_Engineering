import math;

# Dual number: (value, derivative)
# (2, 1) means: value is 2, derivative w.r.t. x is 1

# Arithmetic rules:
# (a, a') + (b, b') = (a+b, a'+b')
# (a, a') * (b, b') = (a*b, a'*b + a*b')
# sin(a, a')         = (sin(a), cos(a)*a')


# The graident by default is zero because i was inserting a constant like Value(3) so since 3 is a constant number then the gradient is zero
# So i manually have to input the gradient if i am creating a function.

class Value:
    def __init__(self,data,gradient = 0):
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
        return Value(-self.data , -self.gradient);

        
    def __sub__(self, other):
        other = other if isinstance(other,Value) else Value(other);
        
        result = Value(self.data +  (-other.data), self.gradient + (-other.gradient));
        return result;

        
    def __mul__(self, other):
        other = other if isinstance(other,Value) else Value(other);

        result = Value(self.data * other.data)
        result.gradient = self.gradient * other.data + self.data * other.gradient;
        return result;
    
    
    # sin(a) -> cos(a) * a'

    def sin(self):
        return  Value(math.sin(self.data), math.cos(self.data) * self.gradient) ;

    # cos(a) -> cos(a) * a'
    def cos(self):
        return Value(math.cos(self.data), -math.sin(self.data)*self.gradient);


    def __pow__(self, other):
        other = other if isinstance(other,Value) else Value(other);
        result = Value(self.data**other.data);
        result.gradient =( other.data * (self.data)**(other.data -1) ) * self.gradient ;
        return result; 

        
    def tanh(self):
        return Value(math.tanh(self.data), (1- math.tanh(self.data)**2 ) * self.gradient);
        
    def relu(self):
        return Value(self.data,self.gradient) if self.data >= 0 else Value(0,0);
        


        



# def expr(x):
#     return Value(x,1)**2 +  Value(x,1)*3


# # y = x ** 2 + 3 *x 
# result = expr(5) ;


result = Value(2,1).tanh();
result2 = Value(math.pi /2,1).sin();
result3 = Value(math.pi /2,1).cos();

print(f"Using dual numbers the gradient is : {result.data:.4f} , {result.gradient:.4f}");
print(f"Using dual numbers the gradient is : {result2.data:.4f} , {result2.gradient:.4f}");
print(f"Using dual numbers the gradient is : {result3.data:.4f} , {result3.gradient:.4f}");



        
        
        
    
