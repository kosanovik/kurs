# формат вывода
# \ - начало управляющей последовательности escape sequence
# \n - перевод строки (enter)
# \t - табуляция (пробел)
# \x - вывод символа по 2м знакоместам 16-формате (ASCII)
# \u - вывод символа по 4м знакоместам 16-формате (Unicode)
# Burned Again Shell
word1 = "пришел"
word2 = "увидел"
word3 = "победил"
word4 = "27\xB0C" # ACSII

print(word1, word2, word3, sep=", ", end=" -> ")
print(word4)
print("концерт группы \"Кино\"")