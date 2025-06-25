# меняем значения переменных местами
a = 3
b = 5

print ("до")
print("a =", a, "b =", b)

a, b = b, a # swap

print ("после")
print("a =", a, "b =", b)

temp = a
a = b
b = temp