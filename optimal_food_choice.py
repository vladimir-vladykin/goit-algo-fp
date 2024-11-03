def main():
    budget = 100
    food_items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    total_calories, money_spent, choosen_products = greedy_algorithm(budget, food_items)
    print(f"Greede result, total_calories: {total_calories}, money spent: {money_spent}, products are:\n{choosen_products}")


def greedy_algorithm(budget, items):
    items = dict(items)

    total_calories = 0
    budget_left = budget
    result = []


    # for item, details in items:

    while budget_left > 0 and items:

        best_item = pop_best_available_item(budget_left,items)
        if best_item is None:
            # probably we're out of budget alredy, not enough money to buy anything more
            break

        budget_left -= best_item[1]["cost"]
        total_calories += best_item[1]["calories"]

        result.append(best_item[0])

    total_budget = budget - budget_left
    return total_calories, total_budget, result

# pop from dict item with max calories
def pop_best_available_item(budget_left, items: dict):
    if not items:
        return None
    
    max_item = None
    for item in items.items():
        _, item_details = item
        if item_details["cost"] > budget_left:
            # we can't afford this item
            continue

        if not max_item or (max_item and item_details["calories"] > max_item[1]["calories"]):
            max_item = item
    
    if (max_item is None):
        # seems like we're out of budget
        return None
    
    items.pop(max_item[0])
    return max_item



def dynamic_programming(items):
    pass


if __name__ == "__main__":
    main()
