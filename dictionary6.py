# question 6

dict = {} 

def add(names, birth): 
	dict.update({names: birth}) 


while(True):
    print("\n")
    print("Search a person’s birthday By name-> Press 1 ")
    print("Add a new name and birthday -> press 2 ")
    print("Change an existing birthday -> press 3 ")
    print("Delete an existing name and birthday -> press 4 ")
    print("Press -> 0 to Exit!!! \n")

    num = int(input("Enter Your Choice : "))

    if num == 0:
        break

    elif num == 1:
        name = input("Enter the Name of the person You Want to Search : ")
        flag = 0
        for i in dict:
            if i == name:
                flag = 1
                print(i," : ",dict[i],"\n")
        if flag == 0:
            print("Name Not Found!!! ")
            
    elif num == 2 or num == 3:
        name = input("Enter the Name of the person You Want to Add : ")
        birthday = input("Enter the Birthday of the person : ")
        add(name, birthday)

    elif num == 4:
        name = input("Enter the Name of the person You Want to delete : ")
        dict.pop(name)

    else :
        for i in dict:
            print(i ," : ", dict[i], "\n")
2
