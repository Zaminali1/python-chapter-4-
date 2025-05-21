# Assignment No: 1
# Store following word meaning in dictionary:
# table:"A piece of furniture ","list of facts & figures"
# cat:"a four leg animal"             

# creating :

diction={
    "cat": "a four leg animal" , 
     "table":["A piece of furniture ", "list of facts & figures"]
}  

print(diction)



# Assignment 2 =
# You are given a list of subjects for students assume 1 class room is required for one subject 
# how many classrooms are needed by all students
# list of subjects = Python, Java,C++, python, JavaScript,java ,python,java,C
# sol = As we know set returns unique values so and we need no classrooms for all subject here are mixed
#  repeated subjects we will create set and length of set to know no of class rooms

no_classroom={"python","Java","C++", "python", "JavaScript","Java","python","Java","C"} 
print(len(no_classroom))
# We need five Classroom.


# Assignment No.3
 
# WAP to enter marks of three subjects from the user and store them in a dictionary start with an empty dictionary
# and add one by one. use subject name as key mark as value

dictionar={}
x=int(input("Enter phy:"))
dictionar.update({"phy":x})
y=int(input("Enter chem:"))
dictionar.update({"chem":y})
print(dictionar)

