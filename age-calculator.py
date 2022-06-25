age = input("What is your current age?")
remaining_years = 90 - int(age)
remaining_days = remaining_years * 365
remaining_weeks = remaining_years * 52
remaining_months = remaining_years * 12

print(f"You have {remaining_days} days, {remaining_weeks} weeks, {remaining_months} months left.")

# first find the years left
# then to find the days, multiply the total no.of days in a year with the years left. You will find the days left
# then do the same for weeks and months
# at last use f-string to give output
# (purpose of f-string: it will convert every datatypes to string for concatenation)