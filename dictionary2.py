# question 2
import re

dictionary = {} 

def uniquecharacter(ch): 

	if ch in dictionary: 

		dictionary[ch] += 1

	else: 

		dictionary.update({ch: 1}) 


user_input = input("Enter A String!!! \n")

pat = re.compile(r'[^a-zA-Z]+')
string = re.sub(pat, ' ', user_input).lower()
string = string.replace(" ", "")

for character in string: 
	uniquecharacter(character) 
 

sorted_keys = sorted(dictionary, key=dictionary.get, reverse=True)
for key in sorted_keys:
    print(key, ' : ', dictionary[key])