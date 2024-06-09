# This file contains all the samples for strings related usecase


# partition the string
# the below returns a tuple with "best" " " "technical interview prep course"

input_words = "best technical interview prep course"
print(input_words.partition(" "))
##############################################################

str = "abcdac"

substr = "xda"

print(str.find(substr)) #



# .join() with lists
numList = ['1', '2', '3', '4']

print(' | '.join(numList)) # "1 | 2 | 3, 4"


cars = "BMW-Telsa-Range Rover"

# split at '-'
print(cars.split("-"))


words = "cats dogs lions"
print(words.split())

#################
# https://www.programiz.com/python-programming/methods/string
# https://www.programiz.com/python-programming/methods/string/split

text = 'bat ball'

print(len(text))

# replace 'ba' with 'ro'
replaced_text = text.replace('ba', 'ro')
print(replaced_text)

song = 'Let it be, let it be, let it be, let it be'

# replacing only two occurrences of 'let'
print(song.replace('let', "don't let", 2))

message = 'python is popular programming language'

# number of occurrence of 'p'
print('Number of occurrence of p:', message.count('p'))

# Output: Number of occurrence of p: 4

quote = 'Let it be, let it be, let it be'

# first occurance of 'let it'(case sensitive)
result = quote.find('let it')
print("Substring 'let it':", result)

# find returns -1 if substring not found
result = quote.find('small')
print("Substring 'small ':", result)

# How to use find()
if (quote.find('be,') != -1):
    print("Contains substring 'be,'")
else:
    print("Doesn't contain substring")



quote = 'Do small things with great love'

# Substring is searched in 'hings with great love'
print(quote.find('small things', 10))

# Substring is searched in ' small things with great love'
print(quote.find('small things', 2))

# Substring is searched in 'hings with great lov'
print(quote.find('o small ', 10, -1))

# Substring is searched in 'll things with'
print(quote.find('things ', 6, 20))

####

# .join() with lists
numList = ['1', '2', '3', '4']
separator = ', '
print(' | '.join(numList)) # "1 | 2 | 3, 4"

# .join() with tuples
numTuple = ('1', '2', '3', '4')
print(separator.join(numTuple))

s1 = 'abc'
s2 = '123'

# each element of s2 is separated by s1
# '1'+ 'abc'+ '2'+ 'abc'+ '3'
print('s1.join(s2):', s1.join(s2))

# each element of s1 is separated by s2
# 'a'+ '123'+ 'b'+ '123'+ 'b'
print('s2.join(s1):', s2.join(s1))

# first string
firstString = "PYTHON IS AWESOME!"

# second string
secondString = "PyThOn Is AwEsOmE!"

if(firstString.lower() == secondString.lower()):
    print("The strings are same.")
else:
    print("The strings are not same.")

sentence = "i love PYTHON"

# converts first character to uppercase and others to lowercase
capitalized_string = sentence.capitalize()

print(capitalized_string)

# Output: I love python


message = 'Python is fun'

print(message.startswith('Python'))


#######

message = 'Python is fun'

print(message.startswith('Python'))

cars = 'BMW-Telsa-Range Rover'

# split at '-'
print(cars.split('-'))

text= 'Love thy neighbor'

# splits at space
print(text.split())

grocery = 'Milk, Chicken, Bread'

# splits at ','
print(grocery.split(', '))

# Splits at ':'
print(grocery.split(':'))

######
