import os

file1 = open('abc.txt','w')
l = ["Sas service is unavailable \n","please wait untill Service Restored !!! \n"]
file1.writelines(l)

file1.close()

file_size = os.path.getsize('abc.txt')
print("The size of the file is : ",file_size,"Bytes")