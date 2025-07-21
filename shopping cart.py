item=input("what item you would like to buy?:")
price=float(input("what is the price?:"))
quantity=int(input("how many item have you taken?:"))
total=price*quantity
print(total)
print(f"you have bought {quantity} x {item}/s")
print(f"your total price is {total}")
