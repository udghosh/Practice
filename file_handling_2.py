

file1 = open('abc.txt','w')
l = ["The Sas service is unavailable \n","please wait untill the Service Restored !!! \n"]
file1.writelines(l)

file1.close()

with open ('abc.txt','r') as file:

    text = file.read()
    count = 0
    for word in text.split():
        #word = word.lower()
        if word == 'The' or word == 'the':
            count +=1 
    print(count)