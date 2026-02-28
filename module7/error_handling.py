try:
    result=10/0

except ZeroDivisionError:
    print("Opss! tried to devide with zero!")


fruits = {
    "apple":5,
    "orange":3,
    "banana":7
}

try:
    print(fruits["cherry"])

except KeyError:
    print("The key does not match in the dictionary")


text = "this is not a number"

try:
    text_to_int = int(text)

except Exception as e:
    print("An error occurred", e)

try:
    result = 10/2
except ZeroDivisionError:
    print("Division by 0")
else:
    print("Division successful. Result=", result)

try:
    result = 10/0
except ZeroDivisionError:
    print("we have an error, we cant divide by 0")
finally:
    print("finally blok executed")

def devide_numbers(a,b):
    try:
        result = a/b
        print("The result is:", result)
    except ZeroDivisionError:
        print("You tried to devide by 0")
    except TypeError:
        print("Invalid type for division")
    except Exception as e:
        print("Unexpected error", e)

divide_numbers(10,2)
divide_numbers(10,0)
divide_numbers(10,'2')