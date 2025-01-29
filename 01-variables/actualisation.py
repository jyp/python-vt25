
raise_rate_percentage = 2

def actualise(salary):
    # print("initially:", salary)
    for year in range(2025, 2030+1):
        salary = salary + (salary * raise_rate_percentage / 100)

initial = int(input("What is the salary now?"))
print("after 5 years the expected salary is", actualise(initial))

