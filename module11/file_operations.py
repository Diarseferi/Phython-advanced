import os
file_path = "example"
'''
file_path = "example.txt"
file = open(file_path,"r")

content = file.read()
file.close()



with open(file_path,"r")as file:
    content = file.read()
    print(content)
'''
#reading from files
with open('example',"r")as file:
    content = file.read()#read entire content
    line = file.readline()#Read a single line
    lines = file.readlines()#Read all lines into a list

#writing to Files
with open('example','w')as file:
    file.write("Hello,World")#Write data to a file

lines = ["Hello World!\n","Welcome to Python ADV!\n"]

with open('example','r')as file:
    file.seek(0)
    data = file.read()
    print(data)
#Checking if the file exists
if os.path.exists('example'):
    print("File exists")


with open('example','a')as file:
    file.write("New data appended.")

#reading and writing in some binary data

data=b'This is some binary data'
with open('example','wb')as file:
    file.write(data)

with open('binary_file.bin','rb')as binary_file:
    data=binary_file.read()


