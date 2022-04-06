# asks users how much change is owed
cents = int(input("How much is owed: "))
# finds out how many quarters are owed
quarters = int(cents / 25)
print(f"Quarters: {quarters}")
# updates the amount of cents left
cents -= quarters * 25
# finds out how many dimes are owed
dimes = int(cents / 10)
print(f"Dimes: {dimes}")
# updates the amount of cents left
cents -= dimes * 10
# finds out how many nickels are owed
nickels = int(cents / 5)
print(f"Nickels: {nickels}")
# updates the total change left and finds out how many pennies are owed
pennies = cents - nickels * 5
print(f"Pennies: {pennies}")