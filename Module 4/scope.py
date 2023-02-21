balance=100
def total_cost(price,quantity):
    global balance
    balance=balance-(price*quantity)
def my_cost(price):
    price=price-balance
    return price
total_cost(30,3)
res=my_cost(400)
print(res)
print(balance)