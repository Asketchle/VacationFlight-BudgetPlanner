# Monthly Meal Budget Planner
monthly_budget = float(input("Total monthly food budget: $"))
meals_out = int(input("Meals eating out per month: "))
cost_per_meal = float(input("Average cost per meal out: $"))
eating_out_total = meals_out * cost_per_meal
grocery_budget = monthly_budget - eating_out_total
weeks = int(input("Number of weeks in the month: "))
weekly_grocery = grocery_budget / weeks
daily_budget = monthly_budget / 30
print(f"\n--- Monthly Meal Budget ---")
print(f"Eating out total: ${eating_out_total:.2f}")
print(f"Grocery budget: ${grocery_budget:.2f}")
print(f"Weekly grocery budget: ${weekly_grocery:.2f}")
print(f"Daily food budget: ${daily_budget:.2f}")
