money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month_counter = 0
increase_coefficient = 1 + increase
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while True:
    money_capital += salary
    money_capital -= spend
    if money_capital <= 0:
        break
    spend *= increase_coefficient
    month_counter += 1

print("Количество месяцев, которое можно протянуть без долгов:", month_counter)
