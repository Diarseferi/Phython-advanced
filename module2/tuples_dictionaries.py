#creating dictionaries from tuples
grades = {
    ("John","Math"):5,
    ("Alice","Science"):4,
    ("Bob","History"):3
}
john_math = grades[("John","Math")]
print("john'ss Math grades is:", john_math)

grades[("Alice","Science")] = 5
print("Alice updated Science grade is:",grades[("Alice","Science")])

#creating a list of dictionary keys
keys-list(grades.keys())

sudent,subject = keys[0]
print("first key Student:", student,"Subject:", subject)