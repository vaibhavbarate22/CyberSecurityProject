#list
item1 = str(input("Enter item in char : "))
item2 = int(input("Enter item in int : "))
item3 = float(input("Enter item in float : "))
print("\n")
list = [item1,item2,item3]
print(list[0])
print("\t",list)
print("\n")

list[0]="yashu"
print(list[0])

#slicing of the list
print(list[0:3])

#method of srings
list.append("vaibhav") #append this is used to add any item at end of the list
print(list)

list2=[1,2,5] #sort the list in order 
list2.sort()
print(list2)

list2.reverse()
print(list2)

from itertools import combinations
count=list2.count
print(count)

"""for list, list2 in zip :
    print(f"{list}:{list2}")"""
#print(neww(zip(list,list2)))
list2.insert(2,121212) # TO insert the element in the list at a specific index list.insert(index,element)
print(list2)

pop=list2.pop(3)
''''
'''
print(pop)
''''''

remove=list2.remove(5)
print(remove)

tuple2=input("enter value in tuple : ")
tuple2=tuple(tuple2.split(","))
print(tuple2)

import getpass

tuple2=getpass.getpass("Enter value in tuple : ") #getpass is used to hide the input
''''''
tuple2=tuple(tuple2.split(","))
print(tuple2)

tuple3=(2,3,4,2,4,2,2,2,3,4,5,7,8,9,5,7,4,0)
count2=tuple3.count(2) #this counts the occurence of the number or element in tuple and return the value
print(count2)
index2=tuple3.index(0)
print(index2)

'''
import sys
import getpass
import os

'''

