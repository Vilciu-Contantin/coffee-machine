MENU = {
    "espresso": {
        "ingredients": {
            "apa": 50,
            "cafea": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "apa": 200,
            "lapte": 150,
            "cafea": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "apa": 250,
            "lapte": 100,
            "cafea": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "apa": 300,
    "lapte": 200,
    "cafea": 100,
}


def is_resource_sufficient(order_ingredients):
    """True daca este posibil,False daca nu ajung ingrediente"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Scuzati, nu avem destula {item}.")
            return False
    return True


def process_coins():
    """Returneaza totalul din banutii inserati."""
    print("Please insert coins.")
    total = int(input("Cati banuti de 25?: ")) * 0.25
    total += int(input("Cati banuti de 10?: ")) * 0.1
    total += int(input("Cati banuti de 5?: ")) * 0.05
    total += int(input("Cati banuti de 1?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Returneaza True daca plata este acceptata, false daca nu."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Aici este restul, {change}.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Scuze, nu sunt destuli bani. Banii au fost returnati.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Scade ingredientele cafelei din resurse."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Aici aveti {drink_name}-ul ☕️. Serviti cu placere!")


is_on = True

while is_on:
    choice = input("​Ce ati vrea sa comandati? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Apa: {resources['apa']}ml")
        print(f"Lapte: {resources['lapte']}ml")
        print(f"Cafea: {resources['cafea']}g")
        print(f"Bani: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])





#