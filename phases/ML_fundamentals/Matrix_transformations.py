
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

#lambda^2 - (a+d)*lambda + (determinant) = 0

def eigenvalues_of_matrix_2x2(matrix):
   a,b = matrix.rows[0] ;
   c,d = matrix.rows[1] ;


   trace = a + d;
   det = (a * d) - (b * c);


   discrimenant = trace**2  - (4 * det);

   # Less than zero then its imaginary and has no real solution.
   if discrimenant < 0:
      real = trace  / 2;
      imaginary = (-discrimenant) ** 0.5 / 2;
      return (complex(real,imaginary), complex(real, -imaginary));
   sqrt = discrimenant** 0.5;
   return ((trace +sqrt) /2 , (trace - sqrt) /2 );

def eigenvalues_2x2(matrix,eigenvalue):
   a,b = matrix.rows[0] ;
   c,d = matrix.rows[1] ;

   if b > 1e-10:
    v = Vector([b, eigenvalue -a]);
   elif d > 1e-10:
       v = Vector([eigenvalue - d , c]);
   else:
       if abs(a-eigenvalue) < 1e-10:
           v =Vector([1,0]);
       else:
           v= Vector([0,1]);
   return v.normalize();

    


    

   

     
def reflection_around_y():
    return Matrix([[-1,0],[0,1]])

def scale_2d(sx,sy):
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

    point = Vector([1, 1]);
    angle = math.pi / 4

    rotated = rotation_2d(angle) @ point
    print(f"Rotate (1,0) by 45 deg: ({rotated.rows[0]}, {rotated.rows[1]})")

    scaled = scale_2d(2, 3)@ point 
    print(f"Scale (1,1) by (2,3): ({scaled})")

    # [
    #   [1,1]  @ [1] = [1 * 1 + 1 * 1] =[2]
    #   [0,1]    [1] =  [0 * 1 + 1 * 1]= [1]
    #]
    sheared = shear_2d(1, 0)@ point 
    print(f"Shear (1,1) kx=1: ({sheared})")

    reflected = reflection_around_y()@ Vector([2.0, 1.0])
    print(f"Reflect (2,1) across y: ({reflected})")

    
    R = rotation_2d( math.pi / 2);
    S = scale_2d(2,2);

    rotate_then_scale = S @ R;
    scale_then_rotate = R @ S;

    result1 = rotate_then_scale @ point;
    result2 = scale_then_rotate @ point;

    
    print(f"{rotate_then_scale}")
    print(f"{scale_then_rotate}")

    
    print(f"Rotate 90 then scale : ({result1})")
    print(f"scale then rotate 90 : ({result2})")
    print(f"Same ? {result1 == result2}")

    A = Matrix([[2, 1], [1, 2]]);
    vals = eigenvalues_of_matrix_2x2(A)
    print(f"Matrix: {A}")
    print(f"Eigenvalues : {vals}")

    for val in vals:
        vec = eigenvalues_2x2(A, val)
        result = (A @ vec)
        scaled = [val * vec.components[0], val * vec.components[1]]
        print(f"  lambda={val:.1f}, v={[round(x,4) for x in vec.components]}")
        print(f"    A@v = {[round(x,4) for x in result.rows[0]]}")
        print(f"    l*v = {[round(x,4) for x in scaled]}")

    
if __name__ == "__main__":
    main();
