# Vacation Flight Budget Planner
ticket_price = float(input("Flight cost per ticket: $"))
travelers = int(input("Number of travelers: "))
total_flight = ticket_price * travelers
baggage_fee = float(input("Baggage fee per person: $"))
total_baggage = baggage_fee * travelers
other_costs = float(input("Airport food/parking costs: $"))
total_budget = total_flight + total_baggage + other_costs
cost_per_person = total_budget / travelers
print(f"\n--- Flight Budget Summary ---")
print(f"Flight cost: ${total_flight:.2f}")
print(f"Baggage fees: ${total_baggage:.2f}")
print(f"Other costs: ${other_costs:.2f}")
print(f"Total budget: ${total_budget:.2f}")
print(f"Cost per person: ${cost_per_person:.2f}")
