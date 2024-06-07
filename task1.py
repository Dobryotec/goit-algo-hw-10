import pulp

model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

model += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Limit"
model += 1 * lemonade <= 50, "Sugar_Limit"
model += 1 * lemonade <= 30, "Lemon_Juice_Limit"
model += 2 * fruit_juice <= 40, "Fruit_Puree_Limit"

model += lemonade + fruit_juice

model.solve()

lemonade_quantity = pulp.value(lemonade)
fruit_juice_quantity = pulp.value(fruit_juice)
total_quantity = lemonade_quantity + fruit_juice_quantity

print(f"Кількість Лимонаду: {lemonade_quantity}")
print(f"Кількість Фруктового соку: {fruit_juice_quantity}")
print(f"Загальна кількість: {total_quantity}")