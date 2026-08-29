import numpy as np
import math

def rotation_3d_z(theta):
    #[cos,-sin,0]
    #[sin,cos,0]
    #[0,0,1]
    c, s = math.cos(theta), math.sin(theta)

    return np.array([[c,-s,0],
                     [s, c, 0],
                     [0, 0, 1]
                     ])
    

def rotation_3d_x(theta):
    c, s = math.cos(theta), math.sin(theta)

    return np.array([[1,0,0],
                     [0,c,-s],
                     [0,s,c]
                     ])

theta = np.pi / 4;


# cos(90 + theta) = -sin(theta);
# sin(90 + theta) = cos(theta) + 
R = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta), np.cos(theta)]
    ])


    
point = np.array([1.0,0.0]);
print(f"Rotate ( 1, 0 ) by 45 degress:{ R @ point} ");


S = np.diag([2,3]);
composition = S @ R;


print(f"Scale(2,3) after Rotate(45): {composition @ point}")


A = np.array([[2,1], [1,2]], dtype=float);


eigenvalues, eigenvectors = np.linalg.eig(A);
print(f"\nEigenvalues: {eigenvalues}")
print(f"Eigenvectors (columns):\n{eigenvectors}")


for i  in range(len(eigenvalues)):
    v = eigenvectors[:, i];
    lam = eigenvalues[i];
    print(f" A @ v{i} = {A @ v }, lambda * v{i} = { lam * v}");
    
print(f"\n det(R) = { np.linalg.det(R):.4f}");
print(f"\n det(S) = { np.linalg.det(S):.1f}");


# Read about change of basis 
# And under stand V @ eigenvalues @ V^-1



B = np.array([[3, 1], [0, 2]], dtype=float)
vals, vecs = np.linalg.eig(B)
D = np.diag(vals)
V = vecs
reconstructed = V @ D @ np.linalg.inv(V)
#  A ^ 100 
print(f"\nEigendecomposition A = V @ D @ V^-1:")
print(f"Original:\n{B}")
print(f"Reconstructed:\n{reconstructed}")



point_3d = np.array([1.0, 0.0, 0.0])
rotated_z = rotation_3d_z(np.pi / 2) @ point_3d
rotated_x = rotation_3d_x(np.pi / 2) @ point_3d

print(f"\n3D point: {point_3d}")
print(f"Rotate 90 around z: {np.round(rotated_z, 4)}")
print(f"Rotate 90 around x: {np.round(rotated_x, 4)}")