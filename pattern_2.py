n = int (input(" Enter A Number N :"))
sum = 0
j = 1
for i in range(1, n + 1): 
    sum = sum + j 
    j = (j * 10) + 1
          
print(" Sum is: ",sum)