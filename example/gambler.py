from collections import deque

money = [int(el) for el in input().split()]
price = deque([int(el) for el in input().split()])

buy_food = 0

while money and price:
    current_money = money[-1]
    current_price = price[0]

    if current_money >= current_price:
        difference = current_money - current_price
        money.pop()
        if money:  # Check if money list is not empty before updating
            money[-1] += difference
        price.popleft()
        buy_food += 1
    else:
        money.pop()
        price.popleft()

if buy_food >= 4:
    print(f"Преглътнал се за деня! Хенри изяде {buy_food} храни.")
elif buy_food > 0:
    if buy_food == 1:
        print(f"Хенри изяде: {buy_food} храна.")
    else:
        print(f"Хенри изяде: {buy_food} храни.")
else:
    print("Хенри остана гладен. Ще опита пак през следващия уикенд.")
