# Set-এ elements যোগ করা

my_set = {1, 2, 3}
my_set.add(4)
# print(my_set)  # {1, 2, 3, 4}

# update()

my_set.update([5, 6, 7])
# print(my_set)  # {1, 2, 3, 4, 5, 6, 7}


# remove
my_set.remove(4)
# print(my_set)


# discard
my_set.discard(7) #{1, 2, 3, 5, 6}
# print(my_set)


# pop
my_set.pop()  # একটি random element মুছে ফেলবে
print(my_set)


# clear
my_set.clear()
print(my_set)  # খালি সেট