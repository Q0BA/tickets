tickets = int(input("Введите количество покупаемых билетов: "))
total = 0
for i in range(tickets):
    age = int(input(f'Возраст {i+1} человека: '))
    if age < 18:
        total += 0
    elif 18 <= age < 25:
        total += 990
    else:
        total += 1390
if tickets > 3:
    discount = 0.9
else:
    discount = 1
print("Сумма к оплате: ", total * discount)