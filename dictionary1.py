# question 1

import re 

dict = {} 

def uniqueWord(Word): 

	if Word in dict: 

		dict[words] += 1

	else: 

		dict.update({words: 1}) 


user_input = input("Enter A String!!! ")
string = user_input.lower()
	
ListOfWords = string.split()

for words in ListOfWords: 
	uniqueWord(words) 
 
for elements in dict: 
	if dict[elements] == 1: 
		print(elements) 
