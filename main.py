# Кортеж (tuple, immutable) не изменямый список
# Функция enumerate() - в цикле for  возвращает пару (i, v)


fio = ['петров', 'сидоров', 'иванов']

# for item in enumerate(fio):
# print(item)
for i, v in enumerate(fio):
    print(f'{i +1}. {v}.')

# python.org