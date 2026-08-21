import random;
import numpy as np
random.seed(42);

from  Vector import Vector;
class Matrix:
    def __init__(self,rows) -> None:
        self.rows = [list(row) for row in rows];
        self.shape = [ len(self.rows), len(self.rows[0]) ];

    def __add__(self, other):
        return Matrix(
            [self.rows[i][j] + other.rows[i][j] for i in range(self.shape[0])]
            for j in range(self.shape[1])
        )
    def __sub__(self, other):
        return Matrix(
            [self.rows[i][j] - other.rows[i][j] for i in range(self.shape[0])]
            for j in range(self.shape[1])
        )
    def scalar_mult(self,scalar: int | float):
        return Matrix([ self.rows[i][j] * scalar for j in range(self.shape[1]) ]
        for i in range(self.shape[0])
        )
    def elemet_wise_multiply(self, other):
        return Matrix(
            [self.rows[i][j] * other.rows[i][j] for j in range(self.shape[1])]
            for i in range(self.shape[1])
        )



            
        
        
                
    def __matmul__(self, other):
        if(isinstance(other,Vector)):

            return Vector(
                [
                    sum(self.rows[i][j] * other.components[j] for j in range(self.shape[1]) )
                    for i in range(self.shape[0])
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

       
    def determinant(self):
        if self.shape == [1,1]:
            return self.rows[0];

        if self.shape == [2,2]:
            return (self.rows[0][0] * self.rows[1][1]) - (self.rows[0][1] * self.rows[1][0])


        det = 0;

        for j in range(self.shape[1]):
            cofactor = ((-1) ** j);
            multipler = self.rows[0][j];
            minor = [];
            # one skips the row
            for row in range(1,self.shape[0]):
                minor_row = [];
                for col in range(self.shape[1]):
                    # this skips the column
                    if col != j:
                        minor_row.append(self.rows[row][col]);
                minor.append(minor_row)
            minor_matrix = Matrix(minor);
            det += cofactor * multipler * minor_matrix.determinant();
        return det;


        # det = 0;
        # for j in range(self.shape[1]) :
        #     minor = Matrix([
        #         [self.rows[i][k] for k in range(self.shape[1]) if k !=j]
        #         for i in range(1,self.shape[0])
        #     ])
        #     det += ((-1) ** j) * (self.rows[0][j] * minor.determinant());
        # return det;

        
    def inverse_2x2(self):
        if self.shape != [2,2]:
            return "This Matrix is not 2 x 2"
        deter = self.determinant();
        mat_copy = Matrix(
            [self.rows[i][j] for j in range(self.shape[1])]
            for i in range(self.shape[0])
        )

        # swap diagonal
        mat_copy.rows[0][0] , mat_copy.rows[1][1] = mat_copy.rows[1][1] , mat_copy.rows[0][0];

        # change sign of other diagonal
        mat_copy.rows[0][1] *= -1;
        mat_copy.rows[1][0] *= -1;

        
        for row in range(mat_copy.shape[0]):
            for col in range(mat_copy.shape[1]):
                mat_copy.rows[row][col] = mat_copy.rows[row][col] / deter;
        
        return mat_copy

               
    def __repr__(self) -> str:
       return  f"Matrix({self.rows}"
                    

def main():
    # weights = Matrix([[random.gauss(0,0.1) for _ in range(3)] for _ in range(2)])
    # input_vector = Vector([1.0,0.5,-0.3]);

    # print(f"Weights : {weights}")
    # print(f"input_vector : {input_vector}")

    # output = weights @ input_vector;

    # print(f"Input (3D): {input_vector}");
    # print(f"Output (2D): {output}");

    # print("This is what a neural neowrk layer does -- matrix multiplication")



    mat = Matrix([
        [1,2],
        [2,-1],
        ])
    print(mat.inverse_2x2())





if __name__ == "__main__":
    main();






