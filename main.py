# Кортеж (tuple, immutable) не изменямый список
# Методы строки split() - преобразование строки в список и join() - преобразование списка в строку

text = "p   t   y no  h  "


res = "".join(text.split()) # убрать все пробелы

print(res)

# ДЗ
# stop_list = []
# слова из стоп листа не попадают в список. список номерованный
# вводится текст, стоп лист и получившийся список слов (сортированный по алфавиту без повторов) - стоп_слова убрать в конце

# ДЗAdd commentMore actions


# Фраза: ну я типо вообще короче не понимаю этот язык

stop_words = ['ну', 'типо', 'короче']


temp = []


stop_words = {'ну', 'типо', 'короче', 'не'}
message = input('Введите сообщение: ')
lst = message.split() # все слова
for item in lst:
    if item not in stop_words:
        temp.append(item)
res = sorted(temp)
res = sorted(set(lst) - stop_words)
for a, b in enumerate(res, 1):
    print(f'{a}. {b}')