age = 18

if age>=18:
    print("you can vote")
else:
    print("you  can not vote")


temperatura=28

if temperatura>30:
    print("its a hot day, stay hydrated.")
elif temperatura>=20 or temperatura <=30:
    print("the weather is pleasant.")
else:
    print("its a cold day")

student_gpa= 4.5
student_score=75

if student_gpa >=3.5:
    if student_score>=50 | student_score<=65:
        print("student with these scores are eligiable for a partial scholar ship")
    elif student_score>65:
        print("student with these scores are eligiable for a scholar ship")
    else:
        print("student gpa and test score are not eligiable for a scholarship")
else:
    print("student gpa and test score are not eligiable for a scholarship")