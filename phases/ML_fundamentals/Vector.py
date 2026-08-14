import math;
class Vector:
    def __init__(self,components):
        self.components = list(components);
        self.dimensions = len(self.components)
    def __add__(self, other):
        return Vector([a+b for a,b in zip(self.components,other.components)]);

    def __sub__(self, other):
        return Vector([a - b for a, b in zip(self.components, other.components)])

    # def dot(self,other):
    #     result = 0;
    #     for a,b in zip(self.components,other.components):
    #         result += a*b
    #     return result;
    def dot(self,other):
        return sum([a * b  for a,b in zip(self.components,other.components)]);

    def magnitude(self):
        return math.sqrt(sum([component ** 2 for component in self.components]));
    def normalize(self):
        mag = self.magnitude();
        return Vector([component / mag for component in self.components])
    def cosine_similarity(self,other):
        return self.dot(other)/ (self.magnitude() * other.magnitude());


    def __repr__(self) -> str:
        return f"{self.components}";

def main():
    
    a = Vector([1,0,0]); 
    b = Vector([0,1,0]);
    # a = Vector([1, 2, 3])
    # b = Vector([4, 5, 6])

    # print(f"a + b = {a + b}")
    # print(f"a · b = {a.dot(b)}")
    # print(f"|a| = {a.magnitude():.4f}")
    # print(f"cosine similarity = {a.cosine_similarity(b):.4f}")


    print (a.dot(b));

if __name__ == "__name__":
    main();


