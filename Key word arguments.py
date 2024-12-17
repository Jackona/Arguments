#key word argument = preceded by an identifier
# helps with readability

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")


#hello("Hello", "Mr." , "Jack", "Stylianou")

#keyword
hello("Hello", title="Mr." , first="Jack", last="Stylianou")