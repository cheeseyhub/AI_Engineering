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


def scaling_unit_square_matrix(kx, ky):
    return np.array([
        [kx,0],
        [0,ky],
    ]
        )

def shearing_unit_square_matrix(xshear=0,yshear =0):
    return np.array([
        [1,xshear],
        [yshear,1],
    ])
    
def rotation_unit_square_matrix(theta):
    c,s = math.cos(theta),math.sin(theta)
    return np.array([
        [c,-s],
        [s,c]
    ])
        
print("Scaling by (2,2)")
print(scaling_unit_square_matrix(2,2) @ unit_square)

print("Shearing by (2) on the y basis vector")
print(shearing_unit_square_matrix(2) @ unit_square)

print("Rotation by 90 degrees")
print(np.round(rotation_unit_square_matrix(math.pi / 2) )@ unit_square)



