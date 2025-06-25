# Interable object
# len() - сколько элементов в объекте

a = 123456 # int - не является iterable

length = len(str(a)) # поэтому конвертируем в str

print(length)

word = input("введите слово для анализа длины: ")
if not word or len(word) < 4:
    print("вы ничего не ввели или слово слишком короткое")
if len(word) > 3:
    print("длина слова",""+ word + "", "=", len(word))