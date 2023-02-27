print ("This program will calculate how much money you would save if you stopped smoking today.")

cigPrice = 0.43

dailyCigs = int(input("How many cigarettes do you smoke per day> "))
dailySavings = round(dailyCigs * cigPrice,2)
weeklySavings = round(dailySavings * 7,2)
monthlySavings = round(weeklySavings * 4,2)
yearlySavings = round(monthlySavings * 12,2)


print ("You could save £", dailySavings, "per day.")
print ("You could save £", weeklySavings, "per week.")
print ("You could save £", monthlySavings, "per month.")
print ("You could save £", yearlySavings, "per year\n")

