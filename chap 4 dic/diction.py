# Dictionary In Python:
# Dictionary is a collection of key-value pairs.
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is unordered, mutable(changeable) and indexed.
# In Python dictionaries are written with curly brackets, and they have keys and values.

# Creating a Dictionary

dict={
      "key":"value",
     "name":"Zamin",
     "age":17.5,
     "marks":[90,76,88,92],
     "grade":"A1"
}
dict["name"]="Hubdar "
print(dict)

# we can also create a nested dictionary
# Nested Dictionary: A dictionary inside another dictionary is called a nested dictionary.
dicti={
       "student1":{
           "name":"Zamin",
           "age":17,
           "marks":[78,82,89,83],
           "class":"8C"
       }
}
# nested are used to store more than one dictionary in a single dictionary.
# we also can type cast the dictionary into a list.
# Dictionary to List
print(list(dicti.values()))


dicte={
    "name":"",
    "profession":"Student",
    "class":5
}
dicte["name"]=input("Enter your name: ")
print(dicte)

# Dictionary Methods
# 1= .keys(): it will return all keys in the dictionary.
print(dicte.keys())
# we can also convert the keys into a list.
print(list(dicte.keys()))

# 2= .values(): it will return all values in the dictionary.
print(dicte.values())

# 3= .items():it will return all items in the dictionary.
print(dicte.items())
# it will return a list of tuples, where each tuple is a key-value pair. 


# 4= .get():it will return value according to key like:
print(dicte.get("profession")) #it will return value of profession

#.update(): it will update dictionary with new key-value pair.
dicte.update({"class":9})
dicte.update({"city":"Bhan"})
print(dicte)


