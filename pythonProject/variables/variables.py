# python variables


myName = "Md. Abdul Khalek"
myAge = 30
myDepartment = "CSE"

print(myName,myAge,myDepartment)
# output : Md. Abdul Khalek 30 CSE

#  Assign Multiple Values
name , age , department = "Raju" , "28" , "CSE"
print(name,age,department)
# Raju 28 CSE


a = b = c = 1200
print(a,b,c)
# output : 1200 1200 1200


# type casting
firstNumber = 100
secondNumber = 200

if firstNumber > secondNumber:
    print(str(firstNumber) + " is greater than " + str(secondNumber))
else:
    print(str(firstNumber) + " is less than " + str(secondNumber))

# output : 100 is less than 200

# Unpack a Collection

fruits  = ["Apple" , "Orange", "Mango"]

firstFruit , secondFruit , thirdFruit = fruits
print("Second Fruit is " + secondFruit) # output: Second Fruit is Orange
print("First Fruit is " + firstFruit) # output: First Fruit is Apple
print("Third Fruit is " + thirdFruit) # output: Third Fruit is Mango


sdfsdf