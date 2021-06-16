# question 4

import re 

dict1 = {} 
#dict2 = {}

def uniqueWord(Word, dictionary): 

	if Word in dictionary: 

		dictionary[words] += 1

	else: 

		dictionary.update({words: 1}) 


user_input = input("Enter A String!!! ")
user_input2 = input("Enter A String to be Matched!!! ")
string = user_input.lower()
string2 = user_input2.lower()
	
ListOfWords = string.split()
ListOfWords2 = string2.split()

for words in ListOfWords: 
	uniqueWord(words, dict1) 

#for words in ListOfWords2: 
#	uniqueWord(words, dict2)
 

for element1 in dict1: 
    for element2 in ListOfWords2: 
        if element1 == element2:
            print(element2)
