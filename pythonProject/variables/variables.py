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
# print("Second Fruit is " + secondFruit) # output: Second Fruit is Orange
# print("First Fruit is " + firstFruit) # output: First Fruit is Apple
# print("Third Fruit is " + thirdFruit) # output: Third Fruit is Mango
#

# Bitwise Operations


# Bitwise AND:

b = 20
a = 10

result = a & b
print("Bitwise AND : " + str(result))

# Bitwise OR:

result = a | b
print("Bitwise OR: "+ str(result))

# যোগ (Addition):

img_a = 3+4j
img_b = 1-2j

print(img_a + img_b)


# List
mixed_list = [25,"hello",3.25,True]
print(mixed_list)


# List-এর গুরুত্বপূর্ণ অপারেশনসমূহ:

# 1. Index
print(mixed_list[0])
print(mixed_list[1])

# 2. Negative Indexing:
print(mixed_list[-2])
print(mixed_list[-1])

# 3. Slicing:
my_list = [10, 20, 30, 40, 50]
print(my_list[1:3])
print(my_list[:3])
print(my_list[2:])

# 4. আইটেম পরিবর্তন (Item Modification):
print(my_list)
my_list[0] = 50
print(my_list)

# 5. আইটেম যোগ করা (Adding Items):

my_list.append(100)
print(my_list)

# insert() মেথড ব্যবহার করে নির্দিষ্ট index-এ নতুন আইটেম যোগ করা হয়।

my_list.insert(2,500)
print(my_list)

# 6. আইটেম মুছা (Removing Items):
# 6.1 remove()
my_list1 = [1, 2, 3, 4]
my_list1.remove(3)  # 3 মুছা হলো
print(my_list1)  # Output: [1, 2, 4]


# 6.2 pop() মেথড দিয়ে index অনুযায়ী আইটেম মুছা হয়, আর কোনো index না দিলে এটি শেষ আইটেম মুছে ফেলে।
pop_item = my_list.pop(2)
print(pop_item)

# 7. List Concatenation:

list1 = [1, 2, 3]
list2 = [4, 5]
combined_list = list2 + list1
print(combined_list)

# 8. আইটেমের উপস্থিতি চেক করা (Check Item Presence): in এবং not in অপারেটর ব্যবহার করে চেক করা যায় কোনো আইটেম list-এ আছে কিনা।

my_list = [1, 2, 3, 4]
check_presence = 8 in my_list
if check_presence:
     print(check_presence)
else:
    print(check_presence)
print(5 not in my_list)  # Output: True


# 9. List-এর দৈর্ঘ্য (Length of List): len() ফাংশন দিয়ে list-এর দৈর্ঘ্য (কতগুলো আইটেম আছে) জানা যায়।

print(len(my_list))


# List Comprehension: List comprehension একটি সংক্ষিপ্ত উপায় যা দিয়ে আমরা একটি list তৈরির জন্য একটি loop বা শর্তাবলীর ব্যবহার করতে পারি।
# সাধারণ loop দিয়ে
comprehension_list = []

for i in range(1,6):
    comprehension_list.append(i**2)

print(comprehension_list)

# List comprehension দিয়ে
comprehension_list1 = [ i**2 for i in range(1,9)]
print(comprehension_list1)



# 4. Item modification (Possible with lists inside tuples): যেহেতু tuple immutable, তাই tuple-এর আইটেম পরিবর্তন করা সম্ভব নয়। তবে যদি tuple-এর মধ্যে কোনো mutable ডেটা টাইপ (যেমন list) থাকে, তাহলে সেই mutable ডেটা পরিবর্তন করা যেতে পারে।


my_tuple = (1, 2, [10, 20])

my_tuple[2][1] = 500
print(my_tuple)


# 7. Tuple Unpacking:

my_tuple1 = (10, 20, 30)
a, b, c = my_tuple1

print(my_tuple1[0])

# Tuple ব্যবহার করার উদাহরণ:

def get_student_info():
    name = "Alice"
    age = 22
    grade = "A"
    return (name, age, grade)  # Tuple হিসেবে মানগুলো ফেরত দেয়া

info = get_student_info()
print(info)  # Output: ('Alice', 22, 'A')

# Tuple unpacking
name, age, grade = info
print(f"Name: {name}, Age: {age}, Grade: {grade}")


# Set তৈরি করার উপায়

my_set = {1, 2, 3, 4}
print(my_set)

# set() কন্সট্রাক্টর ব্যবহার করে
another_set = set([5, 6, 7])
print(another_set)
