def add_list(li) :
    sum = 0
    for x in range(0,len(li)) :
        sum = sum + li[x]
    return(sum) 

li = [1,2,3,4,5,6,7]
print(add_list(li))

"""
# Python program to find sum of elements in list

# creating a list
list1 = [11, 5, 17, 18, 23]

# using sum() function
total = sum(list1)

# printing total value
print("Sum of all elements in given list: ", total)
"""