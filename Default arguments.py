#default argument = default values for certain parameters
#its used when that argument is omitted
#makes functions more flexible, reduces # of arugments
#1 positional
#2 default
#3 keyword
#4 arbitrary

def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

#print(net_price(500))
#print(net_price(500, 0.1))
#print(net_price(500,0.1,0))
