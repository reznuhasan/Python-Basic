with open("myfile.txt",'w') as file:
    file.write("My name is Rizwan")

with open("myfile.txt",'r') as file:
     readFile=file.readline()
     print(readFile)