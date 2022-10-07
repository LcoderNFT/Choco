min = float(input("Enter min weight of cake: "))
max = float(input("Enter max weight of cake: "))
serving = int(input("Enter serving of CHOCO "))
print()
print("%-15s" % "Wt" + "Price")
i = min
while i <= max:
    # If the weight of the cake is < 3 pounds, the price per pound is 5. If the weight is >= 3 pounds, the price per pound is 4.5.
    if i < 3:
        ppp = 5
    else:
        ppp = 4.5
    # P = (number of servings of chocolate used) * 2.5 + (weight of cake in pounds) * (price per pound)
    P = serving * 2.5 + i * ppp
    print("%-15s" % i + str(P))
    i = i + 0.25
    
   
