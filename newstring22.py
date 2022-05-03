'''
 Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.
'''
def new(string):
    length = len(string)
    if length < 2:
        return ("Empty string")
    return string[:2]+string[length-2:]
    
print(new('Hello world'))