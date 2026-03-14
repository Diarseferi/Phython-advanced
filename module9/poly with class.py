class Dog()
    def __init__(self,name):
        self.name=name

    def sound(self):
        print(f"{self.name} make the sound:Woff!")

class Cat()
    def __init__(self,name):
        self.name = name

    def sound(self):
        print(f"{self.name} make the sound:Meow!")

class Bird()
    def __init__(self,name):
        self.name = name

    def sound(self):
        print(f"{self.name} make the sound:Chirp!")

dog = Dog("Buddy")
cat = Cat("Whiskers")
bird = Bird("Tweetie")

for animal in (dog,cat,bird):
    animal.sound()