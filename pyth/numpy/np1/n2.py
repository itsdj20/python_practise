#Create a 5x5x5 cube of 1's
import numpy as np
x=np.arange(125).reshape(5,5,5)
y=np.ones_like(x)

print(y)