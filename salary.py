salary = float(input("Enter the Salary of the Person: "))
if (salary <= 10000) :
    print(" Clerk ")
elif (salary >10000 and salary<=20000) :
    print(" Operator ")
elif (salary > 20000 and salary <= 35000) :
    print(" Assistant ")
elif (salary > 35000 and salary <= 50000) :
    print(" Manager ")
else :
    print(" Invalid Post ")