
class Employee:
   
   def __init__(self, name, age, salary, date_joining):
      self.name = name
      self.age = age
      self.salary = salary
      self.date_joining = date_joining

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Age: ", self.age, "Salary : ", self.salary,  ", Date of joining: ", self.date_joining,)
    


emp1 = Employee("Priom", 27, 20000, "2012-27-July")
emp2 = Employee("Rakesh", 32, 60000, "2010-01-Aug")
emp3 = Employee("Rajesh", 38, 80000, "2008-15-June")
emp4 = Employee("Bob", 24, 20000, "2017-09-Dec")
emp5 = Employee("Dylon", 45, 400000, "2005-18-Jan")

list = [emp1, emp2, emp3, emp4, emp5 ] 

# Sorting

def sortemp_sal(emp):
    return emp.salary

sorted_salary = sorted(list , key= sortemp_sal)


def sortemp_join(emp):
    return emp.date_joining

sorted_join = sorted(list , key= sortemp_join)

# Display

print("Employee Class Before Sorting:\n")
for i in list:
    i.displayEmployee()

print('\n')
print("Employee Class After Sorting with salary:\n")
for i in sorted_salary:
    i.displayEmployee()


print('\n')
print("Employee Class After Sorting with Date of joining:\n")
for i in sorted_join:
    i.displayEmployee()

