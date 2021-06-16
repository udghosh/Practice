def mul_list(li) :
    sum = 1
    for x in range(0,len(li)) :
        sum = sum * li[x]
    return(sum) 

li = [1,2,3,4,5,6,7]
print(mul_list(li))