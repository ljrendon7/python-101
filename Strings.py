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



#old way of substituting strings
my_string = "I like %s" % "Python"
print(my_string) # 'I like Python'

var = "cookies"
newString = "I like %s" % var
print(newString) # 'I like cookies'

another_string = "I like %s and %s" % ("Python", var)
print(another_string)  # 'I like Python and cookies'

my_string = "%i + %i = %i" % (1,2,3)
print(my_string) # '1 + 2 = 3'

float_string = "%f" % (1.23)
print(float_string) # '1.230000'

float_string2 = "%.2f" % (1.23)
print(float_string2) # '1.23'

float_string3 = "%.2f" % (1.237)
print(float_string3) # '1.24'


#new way of subtstituting strings
print("%(value)s %(value)s %(value)s" % {"value":"spam"})


print("Python is as simple as {0}, {1}, {2}".format("a", "b", "c"))