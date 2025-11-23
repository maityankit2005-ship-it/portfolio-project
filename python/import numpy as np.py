import numpy as np

# Define the matrix E
E = np.array([
    [3, 0, 2],
    [2, 0, -2],
    [0, 1, 1]
])

# Calculate the inverse using numpy
E_inv = np.linalg.inv(E)

print("Matrix E:\n", E)
print("\nInverse of E:\n", E_inv)

# Verification (E × E_inv should give Identity Matrix)
verify = np.dot(E, E_inv)
print("\nVerification (E × E_inv):\n", verify)