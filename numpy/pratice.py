import numpy as np

# 1. 
array1 = np.arange(1, 6) * 10
print(array1)

print("multi with 3", np.multiply(array1, 3))
print("Sum", np.sum(array1))
print("mean", np.mean(array1))

# 2 create array fromt 1->20:
array2 = np.arange(1, 21)

# 3 filter even number:
evenNumber = array2[array2 % 2 == 0]
print("filter even number \n", evenNumber)

print("calculator", np.multiply(array2, array2))

# 4 filter all value >= 7
scores = np.array([5, 7, 8, 4, 9, 6, 3, 10])

scores_greater_7 = scores[scores > 6]
print("scores_greater_7: ", scores_greater_7)

print("AVG", np.mean(scores_greater_7))

#  create new array 
np.random.seed(1)
random_array = np.random.randint(1, 14, 13)
print("randomArray", random_array)

new_array = np.where(random_array >= 7, random_array, 0)
print("new_array", new_array)
#  Mini AI mindset
heights = np.array([150, 160, 170, 180, 190])
weights = np.array([50, 60, 65, 70, 80])

BMIs = weights / ((heights/100)**2)

print("BMIs", BMIs)

# filter BMI > 25
filter_BMI = BMIs[BMIs > 25]

print('filter_BMI', filter_BMI)

# (Cực quan trọng, chuẩn bị cho matrix)

arr = np.arange(1, 13).reshape(3,4)

print("matrix 3x4 \n", arr)

# get value in row 2 column 3
print("get value in row 2 column 3", arr[1, 2])
print("get row 2 and column 3", arr[1, :3])