#x = input("What kind of rental car you would like? >")
#print(x)
#print("We are preparing a car for you, the model will be {}".format(x))

x = input("Enter a number >")
y = input("Enter a second number >")

#don't use try except for everything, use it when you expect to get an exception
try:
    result = (int(x)/int(y))
    #print(int(x)/int(y))
except ZeroDivisionError: #specialized exception, must always come before the general one
    print("Sorry you cannot divide by zero")
except ValueError:
    print("Please use vakues 0 - 9 (Except as a divisor!)")
except Exception:   #general exception
    print("An unknown error has occurred")
else: #runs wheather the answer is OK or not
    #print(int(x)/int(y))
    print(result)
