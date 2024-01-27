for x in range(0,10):
    answer = float(input("enter any number :"))
    ask = input("You Want to convert it on (f)arenhite or (C)elcius ? ").upper()
    if ask == "F":
       fahrenheit = 5/9 * (answer - 32)
       print(f"The fahrenheit of {answer} is {fahrenheit} celsius")
    elif ask == "C":
       celsius = (answer* 9/5) + 32
       print(f"The celsius of {answer} is {celsius} fahrenheit")
    else:
       print("Try again")


