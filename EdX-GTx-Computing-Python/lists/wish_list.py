#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://courses.edx.org/courses/course-v1:GTx+CS1301xIII+1T2018/

Solution attempted by Brindha Lekshmisaran
"""

#Write a function called wish_list. wish_list should have
#four parameters, in this order: 
#
# - a list of strings, representing a list of items on a
#   wish list
# - a string, representing a particular item
# - a float, representing the cost of this item
# - a float, representing your budget
#
#If the item is on the list and you can afford it (cost is
#less than or equal to budget), return the string,
#"You should buy a [item name]!", replacing [item name]
#with the string.
#
#If the item is on the list but you can't afford it,
#return the string, "You should save up for a [item name]!",
#replacing [item name] with the string.
#
#If the item is not on the list, you should return the
#string "You probably don't want to buy a [item name].",
#replacing [item name] with the string.
#
#HINT: You do not need a loop to solve this. You can use
#one, but you don't need one.


#Add your function here!

def wish_list(myLst, string, cost, budget):
     if (string in myLst) and (cost <= budget):
          return "You should buy a " + string + "!"
     elif (string in myLst) and (cost > budget):
          return "You should save up for a " + string + "!"
     else:
          return "You probably don't want to buy a " + string + "."

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: "You should save up for a bugle!"

wish_list_items = ["bugle", "trumpet", "banjo", "tuba"]
selected_item = "bugle"
item_cost = 199.99
budget = 150.00

print(wish_list(wish_list_items, selected_item, item_cost, budget))

'''
#Method from the tutorial:

#First, we define the function:
def wish_list(items, item, cost, budget):
    
    #To make this simpler, we need to pay attention to the
    #order of our conditions. The instructions say that it
    #doesn't matter if we can afford it or not if the item
    #isn't on the wish list, so we should check if it's on
    #the wish list first:
    if item in items:
        
        #If it is, now we should check if we can afford it,
        #and return the corresponding message:
        if cost <= budget:
            return "You should buy a {0}!".format(item)
        else:
            return "You should save up for a {0}!".format(item)
        
    #If it wasn't on the wish list, we don't need to check
    #the price: we go ahead and return this message.
    else:
        return "You probably don't want to buy a {0}.".format(item)
'''