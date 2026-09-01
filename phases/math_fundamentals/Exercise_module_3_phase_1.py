import numpy as np
import math


#(0,1)   # (1,1)
#(0,0)   #(1,0)

unit_square = np.array([
    [0,1, 1 ,0],
    [0,0, 1,1]
]
)


#  (2 * 2) (2 * 4) 


def scaling_unit_matrix(kx, ky):
    return np.array([
        [kx,0],
        [0,ky],
    ]
        )

def shearing_unit_matrix(xshear=0,yshear =0):
    return np.array([
        [1,xshear],
        [yshear,1],
    ])
    
def rotation_unit_matrix(theta):
    c,s = math.cos(theta),math.sin(theta)
    return np.array([
        [c,-s],
        [s,c]
    ])
        
print("Scaling by (2,2)")
print(scaling_unit_matrix(2,2) @ unit_square)

print("Shearing by (2) on the y basis vector")
print(shearing_unit_matrix(2) @ unit_square)

print("Rotation by 90 degrees")
print(np.round(rotation_unit_matrix(math.pi / 2) )@ unit_square)



transformation_matrix =  np.array(
    [
    [4,2],
    [1,3]
    ]
)

eigen_values , eigen_vectors =np.linalg.eig(transformation_matrix);

print(eigen_values)
print(eigen_vectors)



# circle points  2 * 8

circle_points = np.array([
    [math.cos(i * (2 * math.pi / 8)) for i in range(8)],
    [math.sin(i * (2 * math.pi / 8)) for i in range(8)]
])

print("Circle Before coordinates : ")
print(circle_points);

composition_transformation = shearing_unit_matrix(0.3) @ scaling_unit_matrix(1.5,0.8) @ rotation_unit_matrix(math.pi / 6);

print("rotate deter")
rotation = rotation_unit_matrix(math.pi / 6) @ circle_points
print(np.linalg.det(rotation_unit_matrix(math.pi / 6) ))


print("scale deter")
scaling = scaling_unit_matrix(1.5,0.8) @ circle_points
print(np.linalg.det(scaling_unit_matrix(1.5,0.8) ))

print("shear deter")
shearing = shearing_unit_matrix(0.3) @ circle_points
print(np.linalg.det(shearing_unit_matrix(0.3) ))


print("composition deter")
print(np.linalg.det(composition_transformation))






print("Circle After coordinates : rotation by 30 and scaling by 1.5,0.8 and then shearing x by 0.3 ")
print(composition_transformation @  circle_points )




