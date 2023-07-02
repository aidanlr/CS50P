def hello(to="world"):
    print("hello,", to)

def main():
    # Prints "hello, world" using the default 'to' value of world.
    hello()

    # Asks for user's name, assigns it to name var, and uses the var as a paramenter for func hello.
    name = input("What's your name? ")
    hello(name)

main()