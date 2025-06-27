# удаление всех карт кроме туза

cards = {3, 7, "T", "D", "V", "K"}

ace = {"T"}

result = cards - ace
print(result)

t_is = False
# 2й вариант
while cards:
    card = cards.pop()
    if card == "T":
        cards.add(card)
        t_is = True
    else:
        print(cards)

    if t_is and len(cards) == 1
        break
