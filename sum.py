xi = input("Please Enter The Initial Number: ")
xf = input("Please Enter The final Number: ")
x = 0
for i in range(xi,xf,1):
    print("adding " + str(i) + " to the sum")
    x = x + i

print("The sum is: " + str(x))
