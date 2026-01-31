fruits =["apple","banana","cherry"]
#print(fruits)
#fruits[1]="orange"
#print(fruits)

#Tuples
words=("spam","eggs","ham")
#words[1]="sausage" -  kemi ni error nuk mund te ndryshohet nje tuple element
print(words[-2])#printon elementin e dyte nga fundi
print(len(words))#printon gjatesine e tuple

person=("Diar",15,"Engineer")

name,age,profession=person

print(name,"'s age is", age, "and profession is", profession)
