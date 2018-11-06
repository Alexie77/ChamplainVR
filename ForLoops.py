for t in range(10):
    print(t)
    print(t + 1)

print ("program run has ended")

for y in range(11):
    print(str(y) + ": ", end="")
    for x in range(y):
        print("*", end="")
    print() #goes to a new line 