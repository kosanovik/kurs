
print('Витязь на распутье')
print("Налево (L) пойдешь, вольную-волю обретешь...")
print("Направо (R) пойдешь, коня потеряешь...")
print("Прямо (F), сыт и вел будешь...")
choice = input("Куда идем (L, R или F): ")
if choice == "L" or choice == "l":
    print('Вольная воля')
elif choice == "R" or choice == "r":
    print('Конь сбежал')
elif choice == "F" or choice == "f":
    print('Сыт и весел')
else:
    print("Выбор не понятен")


