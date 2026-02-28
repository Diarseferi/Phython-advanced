def challenge(number1,number2,operator):
    if operator =="+":
        return number1+number2
    elif operator == "-":
        return number1-number2
    elif operator == "*":
        return number1*number2
    elif operator == "/":
        return number1/number2
    else:
        raise ValueError("Invalid operator")

try:
    number1= float(input("Type number1:"))
    number2= float(input("Type number2:"))
    operator= input("Type the operator (+,-,*,/):")
    result = challenge(number1,number2,operator)
    print("The result of the operation is", result)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("You tried to divide by 0 ")
except Exception as e:
    print("There is an error",e)
finally:
    print("TThe code was executed")

