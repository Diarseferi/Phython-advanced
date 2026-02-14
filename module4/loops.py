# from numpy.ma.core import maximum
#
# names = ["Erina", "Blina", "Uvejs", "Milot","Diar","Diar B", "Donart"]
#
# for name in names:
#     print(name)
#
# sentence = "Hello Everyone"
#
# for char in sentence:
#     if char.isalpha():
#         print(char)
#
# for number in range(1,10):
#     print(number)
#
#
# numbers = [12,20,33,59,80,19,43]
#
# maximum = numbers[0]
#
# for number in numbers:
#     if number > maximum:
#         maximum = number
#
# print("the maximum vvalue in this array was:", maximum)
from itertools import count

#While loop

count=1

while count<=5:
    print("The number is",count)
    count+=1

#break

numbers=[1,2,3,4,5,6,7,8]
target = 4

for number in numbers:
    if number == target:
        print("target found")
        break

#continue

scores = [68,46,35,78,10,99,50,92]
total = 0
count = 0

mesatarja = 0

for score in scores:
    if score>50:
        total += score
        count+=1
        continue
mesatarja= total/count if count>0 else 0

print("the average score for scores abouve 50 is:",mesatarja)

#Do while

while True:
    user_input = input("Enter a positive number: ")

    if user_input.isnumeric():
        number = int(user_input)

        if number > 0:
            break
    print("input invalid try again")
print("You entered a positive number:", number)

total = 0

for number in range(1,11):
    if number%2==0:
        total+=number
print(total)