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

def num_to_str(num):
    return str(num)



potential_num = string_int("6")

print("6")
print(type(potential_num))
print(type(num_to_str(6)))