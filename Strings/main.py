# String is a sequence of characters used to represent texts.

name = "Suhag S Shetty"
company = 'Capgemini'
message = 'I\'m learning Python'
messages = """Hello, Suhag!
Welcome to Python.
Let's learn strings."""

print(name)
print(company)
print(message)
print(messages)

#  STRIND INDEXING

language = "PYTHON"
print(language[0])
print(language[1])
print(language[2])
print(language[3])
print(language[4])
print(language[5])

# NEGATIVE INDEXING

print(language[-1])
print(language[-2])
print(language[-3])
print(language[-4])
print(language[-5])
print(language[-6])

#  STRING SLICING:- EXTRACTS A PORTION OF A STRING. SYNTAX:- string[start:end]

language = "JAVASCRIPT"
print(language[0:3])
print(language[1:4])
print(language[2:5])

#  FORMATTED STRINGS:- is a way to display many values in a string. THERE ARE 2 WAYS TO FORMAT STRINGS 1: USING F-STRING AND 2: USING NAMESPACES

name = "Suhag S Shetty"
age=23
company = "Capgemini"
print("My name is ",name , " and I am " , age , " years old and I work in" ,  company)

# BASIC F-STRING SYNTAX:-

print("My name is {} and I am {} years old and I work in {}".format(name,age,company))

#  SOME MORE STRING METHODS

mothersName = "Sumana Shetty"
print(mothersName.upper())
print(mothersName.lower())
print(mothersName.title())
print(mothersName.capitalize())

lastName = "      shetty      "
print(lastName.strip())
print(lastName.lstrip())
print(lastName.rstrip())

# .strip() removes whitespace from both ends.
# .lstrip() removes whitespace from the left.
# .rstrip() removes whitespace from the right.

# REPLACING OLD TEXT using .replace(old,new) method

message = "I am learning Java"
updatedMessage = message.replace("Java","Python")
print(updatedMessage)
# I am learning Python

text = "cat cat cat"
updatedText = text.replace("cat","dog")
print(updatedText)
# dog dog dog

#  SEARCHING INSIDE STRINGS using .find() method

email = "suhagshetty07@gmail.com"
print(email.find("@"))
print(email.find("gmail"))
print(email.find("xyz"))

#  COUNT -> counts the number of occurences in out string

print(email.count("s")) 

# STARTS WITH -> RETURNS TRUE OR FALSE

print(email.startswith("suhag"))
print(email.startswith("shetty"))

# ENDS WITH -> RETURNS TRUE OR FALSE

print(email.endswith("com")) 
print(email.endswith("yahoo.com"))

# SPLIT -> .split() seperates string to a list:- by default it splits based on the whitespaces.

skills = "Python Java C++ Javascript"
result = skills.split()
print(result)
# ['Python', 'Java', 'C++', 'Javascript']

# JOINING STRINGS -> .join() method joins strings using a seperator

skills = ["Python","Java","C++","Typescript"]
print(",".join(skills))
# Python, Java, TypeScript


#  TO CHECK IF A TEXT IS PRESENT IN OUR TEXT OR NOT

email = "suhagshetty07@gmail.com"
print("@" in email)
print("yahoo.com" in email)
#  TRUE IF PRESENT AND FALSE IF NOT PRESENT

# ALL IN ONE EXAMPLE