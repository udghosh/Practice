# question3

dict = {'a': '#' ,'e': '@','i': '$','o': '%','u': '!'}
str = input("Enter A String!!! \n")
str1 = ''
for i in str:
    flag =0
    for key in dict:
        if i==key:
            str1+=dict[key]
            flag = 1
            continue
    if(flag == 0):    
        str1+=i
print(str1)