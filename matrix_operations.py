# Matrix operations with Python

A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

print("Matrix A:")
for row in A:
    print(row)

print("\nMatrix B:")
for row in B:
    print(row)

print("\nAddition of matrices:")

C = [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]

for row in C:
    print(row)
