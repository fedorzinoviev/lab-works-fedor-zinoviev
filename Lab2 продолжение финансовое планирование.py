salary = 5000 # Ежемесячная зарплата
spend = 6000 # Траты за первый месяц
months = 10 # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03 # Ежемесячный рост цен
required_capital = 0
current_spend = spend
for _ in range(months):
  shortage = current_spend - salary
  if shortage > 0:
    required_capital += shortage
  current_spend *= (1 + increase)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {int(required_capital)}")