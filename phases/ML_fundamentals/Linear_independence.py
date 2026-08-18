from Matrix import Matrix
from Vector import Vector

def is_linearly_independent(vectors )->bool:
    n = len(vectors);
    dim = len(vectors[0].components)
    matrix = Matrix([v.components[:] for v in vectors])
    rows = [row[:] for row in matrix.rows];
    rank = 0;
    for col in range(dim):
        pivot = None;
        for  row in range(rank,len(rows)):
            if abs(rows[row][col]) > 1e-10: 
                pivot = row;
                break;
        if pivot is None:
            continue;
        rows[rank], rows[pivot] = rows[pivot] , rows[rank];
        scale = rows[rank][col] ;
        rows[rank] = [x / scale for x in rows[rank]];
        for row in range(len(rows)):
            if row != rank and abs(rows[row][col]) > 1e-10:
                factor = rows[row][col];
                rows[row] = [rows[row][j] - factor * rows[rank][j] for j in range(dim)]
        rank +=1;
        

    return  rank == n;

    
def rank(vectors):
    n = len(vectors);
    dim = len(vectors[0].components)
    matrix = Matrix([v.components[:] for v in vectors])
    rows = [row[:] for row in matrix.rows];
    rank = 0;
    for col in range(dim):
        pivot = None;
        for  row in range(rank,len(rows)):
            if abs(rows[row][col]) > 1e-10: 
                pivot = row;
                break;
        if pivot is None:
            continue;
        rows[rank], rows[pivot] = rows[pivot] , rows[rank];
        scale = rows[rank][col] ;
        rows[rank] = [x / scale for x in rows[rank]];
        for row in range(len(rows)):
            if row != rank and abs(rows[row][col]) > 1e-10:
                factor = rows[row][col];
                rows[row] = [rows[row][j] - factor * rows[rank][j] for j in range(dim)]
        rank +=1;
        

    return  rank ;

def project(a,b):
    scaler = a.dot(b);
    return Vector([scaler * x for x in b.components]);

# First vector just normalize it ;
# Then for every other vector subtract the component of the vector 
# that is perpendicular to the other 
# so essentialy current = current - projection on the other vector;
def gram_schimdt(vectors):
    orthonormals = [];
    for vector in vectors:
        current = vector;
        for normal in orthonormals:
            projection = project(current, normal );
            current = current - projection;
        if current.magnitude() < 1e-10:
            continue;
        orthonormals.append(current.normalize());
    return orthonormals;

def main():

        
    v1 = Vector([1, 2, 4]);
    v2 = Vector([2, 4, 8])
    v3 = Vector([9, 99, 101])

    # basis = gram_schimdt([v1,v2,v3]);
    # for i, u in enumerate(basis):
    #     print(f"u{i+1} = {u}")
    #     print(f"  |u{i+1}| = {u.magnitude():.6f}")

    # print(f"u1 · u2 = {basis[0].dot(basis[1]):.6f}")
    # print(f"u1 · u3 = {basis[0].dot(basis[2]):.6f}")
    # print(f"u2 · u3 = {basis[1].dot(basis[2]):.6f}");

    # print(f"|u1| = {basis[0].magnitude()}")
    # print(f"|u2| = {basis[1].magnitude()}")
    # print(f"|u3| = {basis[2].magnitude()}")

    # matrix = [v1,v2,v3]
    # print(rank(matrix))




                
                
        

if __name__== "__main__":
    main();
