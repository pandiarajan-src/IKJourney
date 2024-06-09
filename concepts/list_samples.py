# Simple list examples
def print_items_in_list():
    numbers = [1, 2, 3, 4, 5]
    for num in numbers:
        print(num, end=" ")

############

# https://www.programiz.com/python-programming/methods/list

numbers = [21, 10, 54, 12]

print("Before Append:", numbers)

# using append method
numbers.append(32)
numbers.append(9)
print("After Append:", numbers)

prime_numbers = [2, 3, 5]
print("List1:", prime_numbers)

even_numbers = [4, 6, 8]
print("List2:", even_numbers)

prime_numbers.extend(even_numbers) # list1.extends(list2)

print("List after append:", prime_numbers)

languages = ['Python', 'Swift', 'C++']

languages[2] = 'C'

print(languages)  # ['Python', 'Swift', 'C']

# insert method
vowel = ['a', 'e', 'i', 'u']

# 'o' is inserted at index 3 (4th position)
vowel.insert(3, 'o')

print('List:', vowel)

##############


animals = ['cat', 'dog', 'guinea pig', 'dog']
animals.remove('dog')

print('Updated animals list: ', animals)

# error
#animals.remove('fish')

# Updated animals List
print('Updated animals list: ', animals)

# pop
languages = ['Python', 'Java', 'C++', 'French', 'C']

return_value = languages.pop(3)

print('Return Value:', return_value)

print('Updated List:', languages)

languages.pop()
print(languages)

# del

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# deleting the third item
del my_list[2]

# Output: [1, 2, 4, 5, 6, 7, 8, 9]
print(my_list)

# deleting items from 2nd to 4th
del my_list[1:4]

# Output: [1, 6, 7, 8, 9]
print(my_list)

# deleting all elements
del my_list[:]

# Output: []
print(my_list)

prime_numbers = [2, 3, 5, 7, 9, 11]

# remove all elements
prime_numbers.clear()

# Updated prime_numbers List
print('List after clear():', prime_numbers)


# Output: List after clear(): []

##############

# create a list
numbers = [2, 3, 5, 2, 11, 2, 7]

count = numbers.count(2)

print('Count of 2:', count)

prime_numbers = [2, 3, 5, 7]

prime_numbers.reverse()

print('Reversed List:', prime_numbers)

prime_numbers = [11, 3, 7, 5, 2]

# sorting the list in ascending order
prime_numbers.sort()

print(prime_numbers)

vowels = ['e', 'a', 'u', 'o', 'i']

vowels.sort(reverse=True)
print('Sorted list (in Descending):', vowels)

#########

# https://www.programiz.com/python-programming/examples/list-slicing

Lst = [50, 70, 30, 20, 90, 10, 50]

# Display list
print(Lst[1:5]) # from index 1 till index 4

# Initialize list
List = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Show original list
print("\nOriginal List:\n", List)

print("\nSliced Lists: ")

# Display sliced list
print(List[3:9:2])

# Display sliced list
print(List[::2])

print(List[::])

# String slicing
String = 'CodingIsFun'

# Using indexing sequence
print(String[1:5])


#########


# input values to list
list1 = [12, 3, 4, 15, 20]

for elem in list1:
    print(elem)

list1.sort()

print(list1)

colors = ["Red", "Black", "Pink", "White"]

colors.append("Blue")  # add --> insert
colors.append("Orange")

for color in colors:
    print(color)


print(len(colors))

for i in range(len(colors)):
    print(colors[i])

if "Grey" in colors:
    print("Yes, present")


list2 = []

list2.append("Abc");

print(list2)

#######







