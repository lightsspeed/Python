numbers = [1, 2, 3, 4]

#Square each numbers

squared = list(map(lambda x : x ** 2, numbers))
print(squared) 

#Format each number with prefix Number

formatted = list(map(lambda x : f"number: {x**2}", numbers))
print(formatted)

#Check if the number is greater than 3

num_3 = list(map(lambda x :  x > 3, numbers))
print(num_3)

