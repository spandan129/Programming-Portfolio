'''A 50% discount applies to all pizza prices on Tuesdays. This discount does not apply to any delivery cost
(see below).

Delivery costs £2.50, unless there are five or more pizzas in the order, in which case it is free.

A discount of 25% of the total price (pizzas plus delivery, if required) is applied if the customer orders via the new
BPP App.

This is in addition to the Tuesday Discount, and is applied after that discount.'''



def main():
    totalprice = quantity * prize
    # Discount on more than 4 pizza 
    if quantity < 5 and delivery == "y":
        totalprice = totalprice + 2.5
    # 50% discount on Tuesday
    if tuesday == "y":
        totalprice = totalprice * 0.5
    #25% discound for order from app
    if app == "y":
        totalprice = totalprice * 0.75
    print("\nTotal Price: £", totalprice,".")

prize = 12
print("```text")
print("BPP Pizza Price Calculator")
print("==========================")
quantity = -1 
Error = False
while quantity not in range(0,10000):
    Error = False
    try:
      quantity = int(input("\nHow many pizzas ordered? "))
    except ValueError:
      print("Please enter a number!")
      Error = True
    if quantity not in range(0,10000) and Error == False:
        print("Please enter a positive integer!")

delivery = input("Is delivery required? ").lower()
while delivery != "y" and delivery != "n":
    print("Please answer 'Y' or 'N'.")
    delivery = input("Is delivery required? ").lower()

tuesday = input("Is it Tuesday? ").lower()
while tuesday != "y" and tuesday != "n":
    print("Please answer 'Y' or 'N'.")
    tuesday = input("Is it Tuesday? ").lower()

app = input("Did the customer use the app? ").lower()
while app != "y" and app != "n":
    print("Please answer 'Y' or 'N'.")
    app = input("Did the customer use the app? ").lower()

main()
