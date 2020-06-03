#create a 5X5 matrix, in which the elements on the borders will be equal to 1, and inside 0.

import numpy as np
x = np.ones((5, 5))
x[1:-1, 1:-1] = 0
print(x)