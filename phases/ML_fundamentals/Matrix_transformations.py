
from Matrix import Matrix
from Vector import Vector
import math;


def reflection_around_axis_2x2(matrix,axis_number= 0):
    if axis_number > 1:
        print("The axis allowed are x-axis (0) and y-axis (1)")
        return;
    if matrix.shape != [2,2]:
        print("The matrix should be 2 x 2")
        return;

    rotated_matrix = [
        [matrix.rows[i][j] * -1 if i != axis_number and j!= axis_number  else matrix.rows[i][j]  for j in range(matrix.shape[1])]
        for i in range(matrix.shape[0])
        ]  


    return Matrix(rotated_matrix)

def reflection_around_x():
    return Matrix([[1,0],[0,-1]])
     
def reflection_around_y():
    return Matrix([[-1,0],[0,1]])

def scaled_2d(sx,sy):
    return Matrix([[sx,0],[0,sy]]);

    
def shear_2d(kx,ky):
    return Matrix([[1,kx],[ky,1]])


def rotation_2d(theta):
    c, s = math.cos(theta), math.sin(theta);
    return Matrix([
         [c,-s]
        ,[s,c]]
                  )



def main() :
    point = Vector([2,1])
    angle = math.pi / 2;

    rotated = rotation_2d(angle) @ point;
    print(rotated)
    
if __name__ == "__main__":
    main();
