from scipy import sparse
import numpy as np

# Create a 2D NumPy array with a diagonal of ones, and zeros everywhere else
eye = np.eye(4)
print('NumPy array:\n{}'.format(sparse.csr_matrix(eye)))