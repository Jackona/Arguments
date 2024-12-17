#*args = pass multiple non ley arguments
#**kwargs = pass multiple keyword arguments


#def add(a, b):
    #return a + b

# this give TypeError: add() takes 2 positional arguments but 3 were given
#print(add(1,2, 3))

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(3,6,9))