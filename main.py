# Спичочные выражения (list comprehension)

# Список квадратов чисел
squares = [i ** 2 for i in range(10)] # так стало (что попадет (i**2) и по какой закономерности (for i in range(10))
# for i in range(10):
#    squares.append(i**2) - было так
print(*squares,sep=", ")
# список квадратов четных чисел
squares = [i ** 2 for i in range(10) if i % 2 == 0] # (что попадет (i**2) и по какой закономерности (for i in range(10) + условие (if i % 2 == 0))
print(*squares,sep=", ")

# произведение i и j

print([i * j for i in range(3) for j in range(3)])

for i in range(3):
    for j in range(3):
        print(i * j)

n = "400 500 600 700 800 900"
approved = [500, 800]
# print([int(i) for i in n.split()]) # split - список
a = [int(i) for i in n.split() if int(i) in approved]
# какие то действия со списком a
print(a)