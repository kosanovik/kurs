# цикл for
# for <переменная>. in iterable object:
#    команды

# word = "поток"

# for ch in word:
#    print(ch)
#                   0       3   1
# итератор range(start, stop, step)

for i in range(0, 101, 5):
# stop не включается
    if i != 15:
        print(i)