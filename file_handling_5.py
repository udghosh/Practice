
file1 = open('abc.txt','w')
l = ["The Sas service is unavailable \n","please wait untill the Service Restored !!! \n"]
file1.writelines(l)

file1.close()

file2 = open('xyz.txt','w')
l = ["This is the second file\n"]
file2.writelines(l)

file2.close()

def remove_lowercase(file1,file2):
    f1 = open(file1)
    txt1=f1.read()
    
    f2=open(file2,'w')
    sentences=txt1.split()
    for word in sentences:
        mixed = not word.islower() and  not word.isupper()
        if mixed:
            f2.write(word)
            f2.write('\n')

remove_lowercase('abc.txt','xyz.txt')
with open ('xyz.txt','r+') as file:

    text = file.read()
    print(text)