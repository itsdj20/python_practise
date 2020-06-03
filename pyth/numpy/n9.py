#change the sign of the numbers in the range from 9 to 15
import numpy as np 
ar=np.arange(20)
ar[(ar>=9) & (ar<=15)] *= -1
print(ar)