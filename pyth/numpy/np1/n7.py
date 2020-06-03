import numpy as np 
arr = np.array(['PHP', 'JS', 'C++'])
ar=np.array(['Python', 'C#', 'NumPy','ad','dsa','kjks'])
result=np.hstack((arr,ar)).reshape(3,3)
print(result.size)