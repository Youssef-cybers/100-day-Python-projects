print("Welcome to the tip calculator.")

tot_bill = input("What was the total bill? $ ")
price = float(tot_bill)

percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
amount = int(percentage)
factor = (amount / 100) + 1

people = input("How many people to split the bill? ")
person = int(people)
answer = (price / person) * factor

print(f"Each person should pay: ${answer}")
