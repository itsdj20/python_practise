#adding a vector in matrix
import numpy as np 
mat=np.array([[1,2,3],[4,5,6],[7,8,9]])
v=np.array([1,1,0])
result=np.empty_like(mat)
for i in range(3):
    result[i, :] = mat[i, :] + v
print(result)