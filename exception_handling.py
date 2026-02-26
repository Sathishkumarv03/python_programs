try :
    val = input("enter a num :")
    n = int(val)
    result = (10 / n)
    print(int(result))
except ValueError :
    print("invalid error")
except ZeroDivisionError :
    print("cannot divide by zero")
    