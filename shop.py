menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750
cupcake_shop_name = "Hamza's Cupcakes"
signature_flavors = ['chocolate fudge', 'cookie',]


def print_menu():
    for key, item in menu.items():
        print("{} - {}".format(key, item))


def print_originals():
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    for cupcake in original_flavors:
        print(cupcake)


def print_signatures():
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    for cupcake in signature_flavors:
        print(cupcake)


def is_valid_order(order):
    if (order in menu) or (order in original_flavors) or (order in signature_flavors):
        return True
    return False


def get_order():
    order_list = []
    order = input("What would you like to order? ")
    while not order == "exit":
        if is_valid_order(order):
            order_list.append(order)
        else:
            print ("Sorry, this item is not in the menu.")
        order = input("What else would you like? Please type 'exit' to complete your order.")
    return order_list


def accept_credit_card(total):
    if total >= 5:
        return True
    else:
        return False


def get_total_price(order_list):
    total = 0
    for order in order_list:
        if order in original_flavors:
            total += original_price
        elif order in signature_flavors:
            total += signature_price
        else:
            total += menu[order]
    return total


def print_order(order_list):
    print("\nYour order is: ")
    for order in order_list:
        if order in original_flavors:
            print("{} - {}".format(order, original_price))
        elif order in signature_flavors:
            print("{} - {}".format(order, signature_price))
        else:
            print("{} - {}".format(order, menu[order]))

    total = get_total_price(order_list)
    print("TOTAL: {}".format(total))

    if accept_credit_card(total):
        print("You can pay using either cash or credit card.")
    else:
        print("Your total is less than 5KD, you can only pay using cash.")
