#Create a varibale called name and assign and text "YouTube" to it
name = "YouTube"     #Variable declared and assigned value
print("The word is: "+name) #Printout the content of the variable
print("Character in index 0 is: "+name[0]) #Print out the character in index position 0
print("Character in index 3 is: "+name[3])
print("Character in index -1 is: "+name[-1])
print("Character in index -2 is: "+name[-2])

#printing characters in range
#print characters in range 1:4 in word "YouTube"
#printing begins with "o" and end with T in index 3
#It will print "ouT"
#Why?
#Because indexing begins from 0
#Y = index 0,
#o = index 1

print("Characters in index 1:4 is: "+name[1:4])

#[1:]-(means from index 1 to the end)
#it will print "outTube"

print("Characters in index 1: is: "+name[1:])

#[:4]-(means from index 0 to index 3)

print("Characters in index :4 is: "+name[:4])

#[3:10]-(means from index 3 to the end despite not have 10 characters)
print("Characters in index 3:10 is: "+name[3:10])

#create a variable (myName)
myName = "Gideon Kiplangat"
print("Your name is: "+myName)

#print the lenght of characters in variable name
print(len(myName))

