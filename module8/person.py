Class Person:
    def __init__(mosha,emri,mbiemri):
        self.mosha = mosha
        self.emri = emri
        self.mbiemri = mbiemri

def greet(self):
    print("mosha e personit",self.mosha,"emri i personit",self.emri, "mbiemri i personit",self.mbiemri)


person1 = Person("18","olt","mustafa")
print(person1.greet())