with open('example', 'r')as file:
    for line in file:
        cleaned_line = line.strip()
        print(cleaned_line)

#splitting lines into words
with open('example','r')as file:
    for line in file:
        words=line.strip().split()
        print(words)

#conatenating strings

name = 'Alice'
age=30

with open('output.txt','w')as file:
    file.write("Name:"+name + "\n")
    file.write("Age:" +str(age) + "\n")

#Formatting Strings

with open('output','w')as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")

#read,process and write data

with open('example','r')as file:
    for line in file:
        cleaned_line = line.strip()
        modified_line = cleaned_line.replace("Line 1", "Line X")
        file.write(modified_line)
