class Vector:
    def __init__(self,components):
        self.components = list(components);
        self.dimensions = len(self.components)
    def __add__(self, other):
        return Vector([a+b for a,b in zip(self.components,other.components)]);

    def __sub__(self,other):
        return Vector([a-b for a,b in zip(self.components,other.components)]);
    def dot(self,other):
        result = 0;
        for a,b in zip(self.components,other.components):
            result += a*b
        return result;