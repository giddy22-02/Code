# Varibales
# using one variable to print the content of different variables
person_info = {
    'firstname': 'Gideon',
    'lastname': 'Kiplangat',
    'country': 'Kenya',
    'city': 'Nairobi',
    'age': '22 Years'
    }
print('Person information: ', person_info)
# concation of variables
first_name = 'Gideon'
last_name = 'Kiplangat'
country = 'Kenya'
city = 'Nairobi'
age = '22 years'
is_married = False
skills = ['HTML', 'CSS', 'JS', 'java', 'Python']
print('First Name: '+first_name+'\n'+'Last name: '+last_name+'\n'+'Country of residence: '+country+'\n'+'City:'+city+'\n'+'Age: '+age)

# ------manipulating the content of a variable
phrase ="Riara Univesrity"                   # variable name
print(phrase)                                # print the content of the variable
print(len(phrase))                           # print the length of the variable
print(phrase.index("U"))                     # print the index position of letter U
print(phrase.index("t"))                     # print the index position of letter t
print(phrase.replace("Riara","Strathmore"))  # Replacing part of the phrase with a different word
print(phrase.upper())                        # Changing the phrase to uppercase
print(phrase.lower())                        # Changing the phrase to lowercase
print(phrase.isupper())                      # Check if the phrase is uppercase
print(phrase.islower())                      # Check if the phrase to lowercase
print(phrase.upper().isupper())              # Change phrase to upper and check if it is upper
print(phrase + " is the best ")              # concate phrase with another string