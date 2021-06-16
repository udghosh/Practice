# question 5

dict = {} 

def add(name, marks): 
	dict.update({name: marks}) 

for i in range(10):
    user_input = input("Enter Name of Student : ")
    marks = int(input("Enter Student Marks : "))
    add(user_input,marks)

count = 1
for elements in dict: 
    if count <= 5: 
        count += 1
        print(elements," -> ",dict[elements]) 
