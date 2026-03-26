import numpy as np

array = np.array([1,2,3,4,5])

array2 = np.array([1,2,3,4,5], dtype='float')

print(array)
print(array2.dtype)
print(array2)

# data 2-dimention
array3 = np.array([ [1,3,5], [2,4,6], [7,8,9], [9,4,6]])

print(array3)
print(array3.shape)
print(array3.ndim)
print(array3.dtype)

# # # # # # # # Create Numpy Array-------------------
# Zeros, ones, empty, full, orange, linspace
zeroArrayInt = np.zeros((2,4), dtype='int')

zeroArrayFl = np.zeros((2,5), dtype='float')
print("This is zeroArrayInt",zeroArrayInt)

print("This is zeroArrayFl",zeroArrayFl)

onesArrayInt = np.ones((3,5), dtype='int')

print("this is a ones array int", onesArrayInt)


onesArrayfl = np.ones((1,5), dtype='float')

print("this is a ones array float", onesArrayfl)

# Arange

arangeArray1 = np.arange(1, 13 , 3, dtype='int')
print(arangeArray1)

arangeArray2 = np.arange(1, 13 , 3, dtype='float')
print(arangeArray2)

# full
fullArrayInt = np.full((3,6), 111, dtype='int')
fullArrayFl = np.full((3,6), 111, dtype='float')

print(fullArrayInt)
print(fullArrayFl)

# linescpace
# start = start value
# next number = (end value - start value) / (number of elements -1) 
# next number = (end value - start value) / (number of elements -1) 
# next number = (end value - start value) / (number of elements -1) 
lineSpaceArrayInt = np.linspace(2, 15, 4, dtype='float')

lineSpaceArrayFl = np.linspace(1, 13, 3, dtype="float")


print('lineSpaceArrayInt', lineSpaceArrayInt)
print('lineSpaceArrayFl',lineSpaceArrayFl)

# Random in Numpy Array >>>>>>------------------->
randomArray = np.random.random((3,5))

print("randomArray",randomArray)

randomArray2 = np.random.random((3,5))

print("randomArray2", randomArray2)


# normal
normalArray = np.random.normal(0 , 3 , (3,5))

print("normalArray", normalArray)

# randint
randIntArray = np.random.randint(1, 5, [3,5])
print("randIntArray",randIntArray)

# rand
randArray = np.random.rand(4,5)
randArray2 = np.random.rand(2,5)
print("randArray", randArray)
print("randArray2", randArray2)


# Array indexing - Slicing in multi dimensional array
array1Dim = np.random.randint(1, 20, 8)

print("array1Dim", array1Dim)
print(array1Dim[4])

# Slicing single dimension value from array1Dim
print("Slicing 3 values from array1Dim", array1Dim[0:4])
# each one element in array1Dim, every 2 element
print("each one element in array1Dim, every 2 element", array1Dim[::2])



arrayMultiDim = np.random.randint(1, 20, [3,5])

print(arrayMultiDim)
# get value index 2 in row 2 and column 3
# row first, col second
print("value index 2 in row 2 and column 3: ", arrayMultiDim[1, 2])
print("value index 2 in row 2 and column 3: ", arrayMultiDim[2, 4])

# get all values from the first 2 rows and 3 columns 
print("Get the first 2 row \n", arrayMultiDim[:2, :])

print("Get the first 3 columns \n", arrayMultiDim[:, :3])

# Reshaping of Arrays And Transpose:

grid = np.arange(1,13)
print(grid)
print(grid.shape)

# reshape make array become array 1D to row and column
matrix1 = grid.reshape(2,6) 
print("matrix1", matrix1)
print(matrix1.shape)

# Transpose row -> column and column -> row
matrixTranspose = matrix1.T
print("matrixTranspose", matrixTranspose)

# Array Concatenation and Spliting
xArray = np.array([1,2,3,4,5])
yArray = np.array([6,7,8,9,10])

concatArray = np.concatenate((xArray, yArray))
print(" concatArray: ", concatArray)

gridArray = np.array([
    [1,2,3],
    [4,5,6]
])
#  Nối 2 array đồng dạng axis = 0 is row and axis = 1 is column
print(np.concatenate([gridArray, gridArray]))
print(np.concatenate([gridArray, gridArray], axis=1))



#  Nối 2 array khác dimention dùng Vstack or hstack
arrayFirst = np.array([1,2,3])
arraySecond = np.array([
    [4,5,6],
    [7,8,9]
])
arrayThird = np.array([
    [1],
    [2]
])
print('concat 2 array different dimention: \n', np.vstack((arrayFirst, arraySecond)))
print('concat 2 array different dimention: \n', np.hstack((arraySecond, arrayThird )))

# Spliting Array:
arraySpl1 = np.arange(1,11)
print("arraySpl1", arraySpl1)
(spl1, spl2, spl3, spl4) = np.split(arraySpl1, [3, 5, 7])
print("get the first 3 element from arraySpl1 \n", spl1)
print("get next 3 element from arraySpl1 \n", spl2)
print("get next 3 element from arraySpl1 \n", spl3)
print("get remain \n", spl4)
