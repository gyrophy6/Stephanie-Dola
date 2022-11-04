import numpy as np
a = np.array([i for i in range (1, 100)])
b = a[::3]
print (b)
c = np.array([sum(a[i:i+3]) for i in range (0, 99, 3)])
print(c)
matrix = c.reshape(11, 3)
print(matrix)

matrix1 = matrix.T
print(matrix1)

d = np.array([i for i in range (-9,2)])
d = d.reshape(11,1)
S = matrix1 @ d
print(S)

print(matrix1[0::2, ::4], "\n")

matrix3 = matrix[1:9:3, :]
print (matrix3)





#print (S[1:4,0:2:2])

