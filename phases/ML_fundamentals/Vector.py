import math;
import numpy as np

class Vector:
    def __init__(self,components):
        self.components = list(components);
        self.dimensions = len(self.components)
    def __add__(self, other):
        return Vector([a+b for a,b in zip(self.components,other.components)]);

    def __sub__(self, other):
        return Vector([a - b for a, b in zip(self.components, other.components)])

    def dot(self,other):
        return sum([a * b  for a,b in zip(self.components,other.components)]);

    def magnitude(self):
        return math.sqrt(sum([component ** 2 for component in self.components]));

    def normalize(self):
        mag = self.magnitude();
        return Vector([component / mag for component in self.components])

    def cosine_similarity(self,other):
        return self.dot(other)/ (self.magnitude() * other.magnitude());

    # a.b = |a||b| costheta
    # theta = cos^-1 (a.b / |a||b|);
    def angle_between(self, other):
        dot = self.dot(other);
        divisor = self.magnitude() * other.magnitude();
        return math.degrees(math.acos(dot / divisor));

        


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


    #print(a.angle_between(b));
    # v1 = Vector([1,2,3])
    # v2 = Vector([1,1,1])
    # a.b = |a||b| costheta
    # print(v1.dot(v2) / v2.magnitude())

    #02 50 dimension matrix
    vectors = [Vector([np.random.random()  for i in range(50)]) for i in range(5)];
    print(len(vectors))


    max_smiliarity = vectors[0].cosine_similarity(vectors[1]);
    vectors_that_are_most_similar = [1,2]
    for i in range(1, len(vectors)):
        current = vectors[i -1].cosine_similarity(vectors[i]);
        if current  > max_smiliarity:
            max_smiliarity = current;
            vectors_that_are_most_similar[0] =vectors[i-1];
            vectors_that_are_most_similar[1] =vectors[i];

    print(max_smiliarity)
    print(vectors_that_are_most_similar)



if __name__ == "__main__":
    main();


