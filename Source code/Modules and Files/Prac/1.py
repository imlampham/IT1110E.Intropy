import numpy as np
a = np.arange(1, 21)
a = a.reshape((5, 4), order='F').reshape(4, 5)
print(a)
