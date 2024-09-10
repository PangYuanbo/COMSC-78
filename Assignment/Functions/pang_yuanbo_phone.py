#Yuanbo Pang
#This program compares two phone plans and determines which is cheaper.
def get_units():
    units = int(input("Enter number of units used: "))
    return units

def calculate_cost(units, base_cost, base_limit, cost_per_unit):
    if units > base_limit:
        extra_units = units - base_limit
        total_cost = base_cost + (extra_units * cost_per_unit)
    else:
        total_cost = base_cost
    return total_cost

def main():
    units = get_units()
    if units < 0:
        print("You cannot have negative units.")
        return


    base_cost1 = 9.38
    base_limit1 = 65
    cost_per_unit1 = 0.045


    base_cost2 = 8.57
    base_limit2 = 50
    cost_per_unit2 = 0.052


    cost1 = calculate_cost(units, base_cost1, base_limit1, cost_per_unit1)
    cost2 = calculate_cost(units, base_cost2, base_limit2, cost_per_unit2)


    print(f"Cost for plan 1: ${cost1:.2f}")
    print(f"Cost for plan 2: ${cost2:.2f}")


    if cost1 < cost2:
        print("Plan 1 is cheaper.")
    else:
        print("Plan 2 is cheaper.")

main()
