numbers = [3,7,2,9,4,10,15]

minimumNumber = min(numbers)
print(minimumNumber)


maximumNumber = max(numbers)
print(maximumNumber)

averageNumber = sum(numbers) / len(numbers)
print(averageNumber)

with open("result.txt", "w") as f:
    f.write(f"max: {maximumNumber}\n")
    f.write(f"min: {minimumNumber}\n")
    f.write(f"average: {averageNumber:.2f}\n")