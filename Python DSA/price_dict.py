shopping_list = ["banana", "orange", "apple"]
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
# Function to calculate the bill
def compute_bill(food):
    total = 0

    for number in food:
        if (stock[number]>0):
            total += prices[number]
            stock[number] -= 1
    return total

print(compute_bill(shopping_list))