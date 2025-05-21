# Set in python.
#Sets are collection of unordered items each element in set must be unique.
# Sets are mutable but elements inside set are immutable .
# we can not add list and dictionary in set.
#  
#creating set:
seet={1,2,3,4,"Hello","world"}
print(seet) #Output is {1, 2, 3, 4, 'world', 'Hello'}
# it print world before hello because sets are unordered.
#set also ignores duplicate values


# syntax for empty sets:

   # sett={}=>This is empty dictionary.

#  we create empty set by giving set keyword with paranthesis
seit=set()
print(type(seit))


seiit={1,2,3}

# Set Methods:

# Method:1=
#           .add()=> it adds element to set.
# Eg:
seiit.add(4) #it will add 4
# if we want to add 4 again it will be ignored. like
seiit.add(4)
print(seiit) #Output: 1,2,3,4




# Method:2

#           .remove() =>it removes element.
# Eg
seiit.remove(2) #2 will be removed
print(seiit)




# Method 3
#           .pop()=> It removes random values.

seiit.pop()
seiit.pop()
print(seiit)




# Method 4
#             .clear()=> it clears whole set and returns empty set.
seiit.clear() #It will return empty set     
print(seiit)#Otuput= set()



 


