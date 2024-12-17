
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    #for value in kwargs.values():
        #print(value, end=" ")
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('postcode')}")




shipping_label("Lord", "Jack", "Stylianou",
               street="99 Fake St.",
               pobox="PO Box #99",
               city="London",
               postcode="N99 9AZ")