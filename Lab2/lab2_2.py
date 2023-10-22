salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
increase_coefficient = 1 + increase
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
money_capital = 0
for month in range(months):
    money_capital += (spend - salary)
    spend *= increase_coefficient
    
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {money_capital:.0f}")
