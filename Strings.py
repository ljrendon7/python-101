my_string = "Welcome to Python!"
another_string = 'The bright red fox jumped the fence.'
a_long_string = '''This is a
multi-line string. It covers more than
one line'''

print(my_string)
print(another_string)
print(a_long_string)

string_one = "My dog ate"
string_two = "my homework!"
string_three = string_one + string_two

print(string_one)
print(string_two)
print(string_three)

my_number = 123
my_string = str(my_number)
print(my_number)
print(my_string)

#String Methods

not_my_string = "luis rendon"
print(not_my_string.upper())

my_string = "This is a string!"
print(dir(my_string))

# [
#   '__add__', '__class__', '__contains__', '__delattr__', 
#   ...
#   ...
#   ...
#  'translate', 'upper', 'zfill'
# ]

print(help(not_my_string.capitalize))

## string slicing
my_string1 = "I like Python!"
print(my_string1[0:1])
print(my_string1[:1])   # 'I'
print(my_string1[0:12]) # 'I like Pytho'
print(my_string1[0:13]) # 'I like Python'
print(my_string1[0:14]) # 'I like Python!'
print(my_string1[0:-5]) # 'I like Py'
print(my_string1[:])    # 'I like Python!'
print(my_string1[2:])   # 'like Python!'