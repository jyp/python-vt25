
raise_rate_percentage = 2

def actualise(salary):
    print("initially:", salary)
    for year in range(2025, 2030+1):
        salary = salary + (salary * raise_rate_percentage / 100)
        print("after raise of year", year , "the expected salary is", salary)

actualise(20000)
actualise(30000)
