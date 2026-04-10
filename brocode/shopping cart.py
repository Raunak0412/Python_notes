# Shopping Cart Problem 

Foods=[]
Prices=[]
total=0

while  True:
    food=input("Enter a food to buy (q to quit): ")
    if food.lower()=="q":
        break 
    else:
        price=float(input(f"Entre the price of {food}: $"))
        Foods.append(food)
        Prices.append(price)

print("-----Your Cart-----")

for food in Foods:
    print(food, end=" ")

for price in Prices:
    total+=price

print()
print(f"Your total is : ${total}")

