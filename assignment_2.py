print("Welcome!")
companyName = input ('What is your company name?')
cableAmount = input ('How many feet of cable do you need installed?')
print(cableAmount)
totalCost = int(cableAmount) *  0.87
print(f"{companyName} Total Cost: {totalCost} feet")
