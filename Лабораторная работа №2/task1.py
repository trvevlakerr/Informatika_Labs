salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

money_capital = 0  # Начальная подушка

for month in range(1, 11):
    deficit = spend - salary  # Дефицит
    if deficit > 0:
        money_capital += deficit
    spend *= (1 + increase)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {round(money_capital)}")