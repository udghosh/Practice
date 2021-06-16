'''  This is A New Dice Simulator     '''

#importing modules
import random
import time

#Function for Rolling of Unbiased Dice
def Unbiased(mini, maxi):

    rolling = "Yes"

    #looping using user input
    while rolling == "Yes":
        
        print(" Rolling the Dice... ")
        time.sleep(2)
        random_num = random.randint(mini, maxi)
        print(" The Value is 😎😎 - ", random_num)

        print('\n')

        rolling = input("Want to roll the Dice Again (Yes/No) ")



#Function for Rolling of Biased Dice
def Biased(mini, maxi):

    print(" Rolling the Dice... ")
    time.sleep(2)

    rolling = "Yes"

    #looping using user input
    while rolling == "Yes":
        values = []

        mid = int((mini + maxi)/2)

        no_of_lower = random.randint(1, 5)
        no_of_upper = random.randint(6, 10)

        while no_of_lower > 0:

            value = random.randint(mini, mid)
            values.append(value)

            no_of_lower -= 1

        while no_of_upper > 0:

            value = random.randint(mid, maxi)
            values.append(value)

            no_of_upper -= 1

        output = random.choice(values)
        print(" The Value is 😎😎 - ", output)

        print('\n')

        rolling = input(" Want to roll the Dice Again (Yes/No) ")


#Input for Dice Structure
print("\n")
print(" Welcome To All New Dice Simulator. " )
print("***********************************")
print("\n")
print(" Please Select the Dice You Want to Play With :- ")
print(" 1. Normal Dice ")
print(" 2. Altered Dice ")
structure = int(input(" Choose 1 or 2 -\n "))

print('\n'*2)

#Maximum and Minimum Value of output in Dice
if structure == 2:
    print(" Input the Value of minimum output and maximum output. ")
    minimum = int(input(" Minimum - "))
    maximum = int(input(" Maximum - "))
    print('\n'*2)
    
elif structure == 1:
    minimum = 1
    maximum = 6

else:
    print(" Sorry, We are Intrupted because of Invalid Input !!")
    

#Input for dice formate
print( " Choose the format of Dice you want to play with :" )
print( " 1. Unbiased - Equal chances of all the outputs in Dice" )
print( " 2. Biased - Greater chances of higher value outputs in Dice" )
dice = int(input(" Select 1 or 2 - \n"))

print('\n'*2)


#Calling the desided function
if dice == 1:
    Unbiased(minimum, maximum)

elif dice == 2:
    Biased(minimum, maximum)

else:
    print(" Sorry 😒😒 We are Interupted because of Invalid Input !!")
