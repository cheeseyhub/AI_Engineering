class Value:
    def __init__(self,data, children=(), op=''):
        self.data = data;
        self.grad = 0.0;
        self._backward = lambda : None 
        self._prev = set(children)
        self._op = op 

    def __repr__(self):
        return f"Value(data={self.data:.4f}, grad={self.grad:.4f})";
