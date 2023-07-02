def main():
    x = int(input("What's x? "))
    y = int(input("What's y? "))
    optr()

    if optr == ("Power") == True:
        print(x, "to the power of", y, "is", x ** y)
    
    elif optr == ("Multiply" or "Multiplication") == True:
        print(x, "multiplied by", y, "is", x * y)
    
    elif optr == ("Divide" or "Division") == True:
        print(x, "divided by", y, "is", x // y)

    elif optr == ("Add" or "Addition") == True:
        print(x, "plus", y, "is", x + y)
    
    elif optr == ("Subtract" or "Subtraction") == True:
        print(x, "-", y, "is", x - y)
    else:
        print("Invalid Operator")
    return
    

def optr():
    optr = input("What's your desired operation? ").strip().capitalize()
    print(optr)

main(0