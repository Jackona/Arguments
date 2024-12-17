#*args = pass multiple non ley arguments
#**kwargs = pass multiple keyword arguments


def print_address(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")


print_address(street="999 Fake Rd.",
              city="London",
              county="London",
              postcode="N99 9AZ")