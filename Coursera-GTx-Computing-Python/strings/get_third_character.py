#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://courses.edx.org/courses/course-v1:GTx+CS1301xIII+1T2018/
"""

#Write function called third_character that accepts a
#string as an argument and returns the third character
#of the string. If the user inputs a string with fewer than
#3 characters, return "Too short". 


#Write your function here!
def third_character(myString):
    if len(myString) >= 3:
        return myString[2]
    else:
        return "Too short"

'''
#Or, we can try to return the third character, and catch
#the error that may arise:

def third_character(input_string):
    try:
        return input_string[2]
    except TypeError:
        return "Too short
'''

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 1, o, and "Too short", each on a different line.
print(third_character("CS1301"))
print(third_character("Georgia Tech"))
print(third_character("GT"))



