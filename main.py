def main():
    food = ["burger","chips","buns","soda"]
    price = [50,100,40,80]
    my_order_food = []
    my_order_cost = []
    counter = 0
    total = 0
    print("Welcome to Kings food and beverages\n")
    order = input("Can I take your order?yes/no")
    if order == "no":
        exit()
    else:
        print("Thank you")
    next_order = True
    while next_order == True:
        food_order = input("Please Enter your order:")
        if food_order =="burger":
            my_order_food.append(food[0])
            my_order_cost.append(price[0])
            counter = counter + 1
            total = total + (price[0])
        elif food_order == "chips":
            my_order_food.append(food[1])
            my_order_cost.append(price[1])
            counter = counter + 1
            total = total + (price[1])
        elif food_order == "buns":
            my_order_food.append(food[2])
            my_order_cost.append(price[2])
            counter = counter + 1
            total = total + (price[2])
        elif food_order == "soda":
            my_order_food.append(food[3])
            my_order_cost.append(price[3])
            counter = counter + 1
            total = total + (price[3])
        else:
            print("Order not in the menu")
        finished = input("Have you finished ordering?")
        if finished == "no":
            next_order = True
        else:
            next_order = False
    print("Here is your order")
    y=0
    while y<counter:
        print("Item: ",(my_order_food[y]))
        print("Cost: $",(my_order_cost[y]))
        y = y+1
    print("The total cost of your order is $", (total))
main()