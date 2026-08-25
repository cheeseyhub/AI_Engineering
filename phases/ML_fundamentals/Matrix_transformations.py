
from Matrix import Matrix
import math;


def reflection_around_axis(matrix,axis_number= 0):
    rotated_matrix = [
        [matrix.rows[i][j] * -1 if i != axis_number and j!= axis_number  else matrix.rows[i][j]  for j in range(matrix.shape[1])]
        for i in range(matrix.shape[0])
        ]  


    return Matrix(rotated_matrix)

     







def main() :
    mat = Matrix([
        [1,0,0],
        [0,1,0],
        [0,0,1]
    ])

    
    print(reflection_around_axis(mat,2))
    
if __name__ == "__main__":
    main();
