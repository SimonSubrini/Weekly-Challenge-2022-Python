import numpy as np
def orthogonalVectors(v1,v2):
    return np.dot(v1,v2)==0

print(orthogonalVectors([1,0],[0,1]))
print(orthogonalVectors([2,1],[-1,2]))
print(orthogonalVectors([2,1],[2,2]))
