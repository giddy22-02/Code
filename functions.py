def greet(lang):
    if lang == "es":
        print("Hola")
    elif lang == "fr":
        print("Bonjour")
    else:
        print("Hello")


greet("fr"),


# using return
def greet_two(language):
    if language == "es":
        return "Hola"
    elif language == "fr":
        return "Bonjour"
    else:
        return "Hello"


print(greet_two("es"), "Gideon")

# finding the largest number in the list
# for loops
largest_so_far = None
for i in [23, 7, 3, 89, 6, 1, 90]:

    if largest_so_far is None:
        largest_so_far = i
    elif i > largest_so_far:
        largest_so_far = i
print("Largest number is", largest_so_far)

# finding the smallest number in the list
smallest = None
for i in [23, 7, 3, 89, 6, 1, 90]:
    if smallest is None:
        smallest = i
    elif i < smallest:
        smallest =i

print("The smallest number is:", smallest)
fruit = "banana"
for letter in fruit:
    print(letter)
    