Class Animal:
    def __init__(self , typeOfAnimal, raca, ngjyra):
        self.typeOfAnimal = typeOfAnimal
        self.raca = raca
        self.ngjyra=ngjyra

 def greet(self):
     print("The type of the animal is", self.typeOfAnimal,".the race is",self.raca, ".and the color is"self.ngjyra)


dog= Animal("Dog","Husky","withe")
cat= Animal("Cat","British","Gray")

print(dog.greet())
print(cat.greet())