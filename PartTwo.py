
x = 0
while x < 75:
    pay = int(input("Please insert coins "))
    amount_due = 75 - pay
    print(amount_due , "pence")
    x = x + pay
print("change due:" , x - 75)    