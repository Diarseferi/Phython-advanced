# from pyexpat.errors import messages
#
#
# def greet ():
#     print("hello world")
#
# greet()
#
# def greet_person(name):
#     print("hello", name)
#
# greet_person("Greta")
#
# def greet2(name)
#     global message
#
#
#     message = f"hello,{name}"
#     print(message)
#
# greet2("Blina")
# print(message)
# #
#
# greeting = "Hello"
# name = "Uvejs"
#
# def greet():
#     global greeting
#     greeting = "Goodbye"
#
#     name = "Dren"
#
#     message = f"{greeting}, {name}"
#     print(message)
#
# greet()
from pyexpat.errors import messages


def greet_person(name,greeting="Hello"):
    message = f"{greeting}, {name}"
    return message

metoda1 = greet_person("Milot")

metoda2 = greet_person("Donart","Hi")

print(metoda1)

print(metoda2)

