import torch
class Value:
    def __init__(self,data, children=(), op=''):
        self.data = data;
        self.grad = 0.0;
        self._backward = lambda : None 
        self._prev = set(children)
        self._op = op 

    def __repr__(self):
        return f"Value(data={self.data:.4f}, grad={self.grad:.4f})";

    def __add__(self,other):
        other = other if isinstance(other,Value) else Value(other);
        out = Value(self.data + other.data , (self,other),"+");
        def _backward():
            self.grad += out.grad;
            other.grad += out.grad;
        out._backward = _backward;
        return out;

    def __mul__(self,other):
        other = other if isinstance(other,Value) else Value(other);
        out = Value(self.data * other.data , (self,other) ,"*");
        def _backward():
            self.grad += other.data * out.grad;
            other.grad += self.data * out.grad;
        out._backward = _backward;
        return out;

    def relu(self):
        out = Value(max(0,self.data),(self,),'relu');
        def _backward():
            self.grad +=(1.0 if out.data > 0 else 0.0) * out.grad;
        out._backward = _backward;
        return out;



