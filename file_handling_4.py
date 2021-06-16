

file1 = open('abc.txt','w')
l = ["The Sas service is a unavailable \n","Can u please wait untill the Service Restored !!! \n"]
file1.writelines(l)

file1.close()

with open ('abc.txt','r') as file:

    text = file.read()
    
    for word in text.split():
        word = word.lower()
        if word == 'a' or word == 'e' or word == 'i' or word == 'o' or word == 'u' :
             
            print(word)