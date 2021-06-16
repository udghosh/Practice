

file1 = open('abc.txt','w')
l = ["Sas service is unavailable \n","please wait untill Service Restored !!! \n"]
file1.writelines(l)

file1.close()

with open ('abc.txt','r') as file:

    text = file.read()
    
    for word in text.split():
        #word = word.lower()
        if word.startswith('s') or word.startswith('S'):
            print(word)