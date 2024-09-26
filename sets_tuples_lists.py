# collection = single "variable" used to store multiple values
# lits = [] ordered and changeable. Duplicates. Ok
# Set = {} unordered and immutable, but Add/Remove Ok. NO duplicates
# Table = () ordered and unchangable. Duplicates Ok/ FASTER\

fruit="apple"

fruits = ["apple", "banana", "coconut", "kiwi", "blueberry"]
#print(dir(fruits)) #prints out all the methoids that come with it
#print(help(fruits))
#print(len(fruits)) 
#print ("apple" in fruits) #True or false of whether something is in there or not

#for fruit in fruits:
#print(fruit)
# NO INDEX USED IN LIST

fruits [1] = "pineapple"
for fruit in fruits:
     print (fruit)
    # YOU CAN CHANGE VALUES USING THE FUNCTION ABOVE
     
fruits.append ("pineapple")
fruits.remove ("apple")
fruits.index (0,"pineapple")
fruits.sort()
fruits.reverse()
fruits.clear()