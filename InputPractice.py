#x = input("What kind of rental car you would like? >")
#print(x)
#print("We are preparing a car for you, the model will be {}".format(x))

x = input("Enter a number >")
y = input("Enter a second number >")

try:
    result = (int(x)/int(y))
    #print(int(x)/int(y))
except ZeroDivisionError:
    print("Sorry you cannot divide by zero")
else: #runs wheather the answer is OK or not
    #print(int(x)/int(y))
    print(result)
