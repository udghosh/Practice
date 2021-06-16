'''
#Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])  
print(thislist[:4]) 
print(thislist[2:])


output:
['cherry', 'orange', 'kiwi']
['apple', 'banana', 'cherry', 'orange']
['cherry', 'orange', 'kiwi', 'melon', 'mango']
'''

'''
#Change Item Value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "Rose"
print(thislist)

output:
['apple', 'Rose', 'cherry']
'''


'''
#Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

output:
Yes, 'apple' is in the fruits list
'''

'''
#To add an item at the specified index, use the insert() method:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

output:
['apple', 'orange', 'banana', 'cherry']
'''


'''
#Add Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

output:
['apple', 'banana', 'cherry', 'orange']
'''


'''
#The pop() method removes the specified index, (or the last item if index is not specified):
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

output:
['apple', 'banana']
'''


'''
#Remove Item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

output:
['apple', 'cherry']
'''


'''
#Example :-The del keyword can also delete the list completely:
thislist = ["apple", "banana", "cherry"]
del thislist

output:
empty
'''


'''
#Example:- The clear() method empties the list:
thislist = ["apple", "banana", "cherry"]
thislist.clear()

output:
empty
'''


'''
#Copy a List
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

output:
['apple', 'banana', 'cherry']
'''


'''
#Join Two Lists
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

output:
['a', 'b', 'c', 1, 2, 3]
'''


'''
#Example:- Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

output:
['a', 'b', 'c', 1, 2, 3]
'''


'''
# Nested List
A=["Happy", [2,0,1,5]]
print(A[0][1])   
print(A[1][3])

output:
a
5
'''


'''
#List Membership Test
my_list = ['p','r','o','b','l','e','m']
print('p' in my_list)
print('a' in my_list)
print('c' not in my_list)

output:
True
False
True
'''

'''
A=[1,2,3,1,2,3,1]
print(A.count(1))

A.reverse()
print(A)

print(max(A))
print(min(A))
print(sum(A))

output:
3
[1, 3, 2, 1, 3, 2, 1]
3
1
13
'''