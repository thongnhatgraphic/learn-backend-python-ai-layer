import numpy as np

a = np.arange(3)

# Create 1 array == size with a andeach element will be add with 5 
print("a", a + 5)

b = np.arange(1,7).reshape(2,3)
print("a \n", a)
print("b \n", b)

# each row of a will be add with each row of b
print("a + b \n", a + b)

# ##### # Manipulating and Comparing arrays:

listNumber = np.arange(1, 4)
print("listNumber", listNumber)
print("sum", sum(listNumber))

#  Create a massive Numpy Array 1D
massiveArray = np.random.random(10000)
# print("massiveArray \n", massiveArray)
print("massiveArray \n", massiveArray[:5])
print("len", massiveArray.size)
print("len", massiveArray.shape)


print(sum(massiveArray)) 
# should be use np.sum because speed calculator faster
print(np.sum(massiveArray))

# STANDARD DEVIATION AND VARIANCE ( Độ lệch chuẩn và phương sai):
print("STANDARD DEVIATION", np.std(np.arange(1,11)))
print("Variance", np.var(np.arange(1,11)))
# Sqrt ( căn bậc 2)
print("Standard deviation", np.sqrt(np.var(np.arange(1,11))))

# Sorting Array:
messyArray = np.array( [5, 6, 3, 9, 1, 8, 2, 7, 4])

print("messyArray: \n", messyArray)

sortMessyArray = np.sort(messyArray)

print("sortMessyArray \n", sortMessyArray)

# show index of each element by root array
print("index of each element: \n", np.argsort(messyArray))

np.random.seed(40)
MatA = np.random.randint(0, 10, (4, 6))

print("MatA \n", MatA)

sortByRow = np.sort(MatA, axis=1)
print("sortByRow \n", sortByRow)

sortByColumn = np.sort(MatA, axis=0)
print("sortByColumn \n", sortByColumn)

# Linear Algebra ( Nhân ma trận):
maxtrixA = np.arange(1, 10).reshape(3,3)

martrixB = np.flip(np.arange(1, 7)).reshape(3,2) # hoặc dùng np.flip(arange(1, 7)) đảo ngược từ lớn đến nhỏ.
print("maxtrixA \n", maxtrixA)

print("maxtrixB \n", martrixB)

# Tích vô hướng
resultLinearAlgebra = np.dot(maxtrixA, martrixB)
resultLinearAlgebra2 = maxtrixA.dot(martrixB)
print("resultLinearAlgebra \n", resultLinearAlgebra)
print("resultLinearAlgebra2 \n", resultLinearAlgebra2)
# Explain above result: Hàng đầu tiên của MaxtriA * Cột đầu tiên của MaxtrixB

dMaxtrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
eMaxtrix = [
    [1,2],
    [3,4],
    [5,6]
]

resultLinear = np.dot(dMaxtrix, eMaxtrix)
print("linear algebra \n", resultLinear)
# Để tuyến tính giữa e và d thì cần transpose e
t_emaxtrix = np.transpose(eMaxtrix)
print("t_emaxtrix \n", t_emaxtrix)
print("new linear algebra \n", np.dot(t_emaxtrix, dMaxtrix))
