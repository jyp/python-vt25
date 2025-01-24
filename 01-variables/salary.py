
# Ask what the user has for salary before taxes
gross_salary = int(input("What is your salary before taxes?"))
# Ask the user for his/her tax percentage.
tax_percentage = int(input("What is tax percentage?"))
# Ask the user for his/her rent.
rent = int(input("Rent amount?"))
# Calculate the taxes by multiplying the salary before taxes with the tax percent.
taxes = gross_salary * tax_percentage / 100
# Calculate the salary after taxes by subtracting the tax.
net_salary = gross_salary - taxes
# Calculate the remaining income by subtracting the rent.
# Show the result to the user.
