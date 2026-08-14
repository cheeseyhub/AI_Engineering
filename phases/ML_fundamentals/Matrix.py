import random;
random.seed(42);

from  Vector import Vector;
class Matrix:
    def __init__(self,rows) -> None:
        self.rows = [list(row) for row in rows];
        self.shape = (len(self.rows), len(self.rows[0]));

    def __matmul__(self, other  ):
        if(isinstance(other,Vector)):
            return Vector(
                [
                    # sum(self.rows[i][j] * other.components[j] for j in range(self.shape[0]) for i in range (self.shape[1]))
                    sum(self.rows[i][j] * other.components[j] for j in range(self.shape[1]) for i in range(self.shape[0]) )
                ]
            )

        rows = [];
        for i in range(self.shape[0]):
            row = [];
            for j in range(other.shape[1]):
                result = 0;
                for k in range(self.shape[1]):
                    result += self.rows[i][k] * other.rows[k][j];
                row.append(result)
                
            rows.append(row);
        return Matrix(rows);
    def tranpose(self):
       rows = [];
       
       for i in range(self.shape[1]):
           row = []
           for j in range(self.shape[0]):
               row.append( self.rows[j][i])
           rows.append(row);
       return rows;

        
               
    def __repr__(self) -> str:
       return  f"Matrix({self.rows}"
                    

def main():
    weights = Matrix([[random.gauss(0,0.1) for _ in range(3)] for _ in range(2)])
    input_vector = Vector([1.0,0.5,-0.3]);

    print(f"Weights : {weights}")
    print(f"input_vector : {input_vector}")

    output = weights @ input_vector;

    print(f"Input (3D): {input_vector}");
    print(f"Output (2D): {output}");

    print("This is what a neural neowrk layer does -- matrix multiplication")
        


if __name__ == "__main__":
    main();






