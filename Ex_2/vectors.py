import numpy as np
from scipy.sparse import diags
import matplotlib.pyplot as plt

# create a null vector of size 10 but the fifth value which is 1
x = np.zeros(10)
x[4] = 1
print(x)

# create a vector with values ranging from 10 to 49
y = np.arange(10, 50)
print(y)

# reverse a vector (first element becomes last)
z = np.arange(0, 10)
z_reversed = np.flip(z, 0)
print(z, z_reversed)

# create a 3x3 matrix with values ranging from 0 to 8
a = np.arange(0, 9).reshape(3, 3)
print(a)

# find indices of non-zero elements from [1,2,0,0,4,0]
b = np.array([1, 2, 0, 0, 4, 0])
non_zero_indices = np.nonzero(b)
print(non_zero_indices)

# create a random vector of size 30 and find the mean value
c = np.random.random(30)
mean = np.mean(c)
print(mean)

# create a 2d array with 1 on the border and 0 inside
n_rows = 5
n_cols = 5
d = np.ones((n_rows, n_cols))
d[1:-1, 1:-1] = 0
print(d)

# create a 8x8 matrix and fill it with a checkerboard pattern
diag = np.ones(8)
checkerboard_1 = diags([diag[0:2], diag[0:4], diag[0:6], diag, diag[0:6], diag[0:4], diag[0:2]], [-6, -4, -2, 0, 2, 4, 6], shape=(8, 8)).toarray()
plt.matshow(checkerboard_1, cmap='gray')
plt.show()

# create a checkerboard 8x8 matrix using the tile function
e = np.array([[0, 1], [1, 0]])
checkerboard_2 = np.tile(e, (4, 4))
plt.matshow(checkerboard_2, cmap='gray')
plt.show()

# Given a 1D array, negate all elements which are between 3 and 8, in place
f = np.arange(11)
negating_multiplier = np.where((f >= 3) & (f <= 8), -1, 1)
f_negated = f * negating_multiplier
print(f, f_negated)

# Create a random vector of size 10 and sort it
g = np.random.random(10)
g_sorted = np.sort(g)
print(g, g_sorted)

# Consider two random array A and B, check if they are equal
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = np.array_equal(A, B)
print(A, B, equal)

# How to calculate the square of each number in an array in place (without creating temporaries)?
Z = np.arange(10, dtype=np.int32)
print(Z.dtype)
Z *= Z
print(Z.dtype)

# How to get the diagonal of a dot product?
P = np.arange(9).reshape(3,3)
Q = P + 1
R = np.dot(P, Q)
S = np.diag(R, k=0)
print(R, S)