
numbers = [1,2,3,4,5]

squares = []

for n in numbers:
    squares.append(n*n)

print(squares)

person = {
    "name": "John",
    "age": 30,
    "price": 10.5
}


print(person["name"])

if person["age"] > 18:
    print("You are an adult")
else:
    print("You are a child")    

numbers = [1,2,3,4,5]

for j in person:
    print(j)

for i in range(5):
    if i > 2:
        print(i)
    else :
        print("less than 3")
