"""
Challenge #3:

Create a function that takes a string and returns it as an integer.

Examples:
- string_int("6") ➞ 6
- string_int("1000") ➞ 1000
- string_int("12") ➞ 12
"""
def string_int(txt):
    # Your code here
   number = int(txt)
   return number


string = "example"
other_string = "also a string"


some_int = 1000

#check the type of a variable 
print(type(string))
print(type(some_int))

print(type(string_int("1000"))