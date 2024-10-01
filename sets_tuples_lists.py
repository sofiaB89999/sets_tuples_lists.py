# collection = single "variable" used to store multiple values
# lits = [] ordered and changeable. Duplicates. Ok
# Set = {} unordered and immutable, but Add/Remove Ok. NO duplicates
# Table = () ordered and unchangable. Duplicates Ok/ FASTER\

fruit="apple"

#LIST
#fruits = ("apple", "banana", "coconut", "kiwi", "blueberry")
#print (fruits.count("coconut"))

#for fruits in fruits:    
    #print (fruits)

# #DICTIONARIES
# #dictionary= a colllection of {key:value} pairs
#                         #ordered and changeable. No duplicates or index
# capitals = {"USA": "Washington DC.",
#             "India" : "New Delhi",
#             "China": "Beijing",
#             "Russia": "Moscow"}
# #print (dir(capitals))
# #print (help(capitals))
# #print (capitals.get ("Russia"))
# if capitals.get ("Russia"):  #CLARIFIES EXISTENCE WITHIN THE DICTIONARY
#     print ("That capitals exist")
# else:
#     print ("That capital doesn't exist")
# capitals.update {("Mexico": "New Mexico")} #ADDS NEW INFO
# capitals.update {("USA": "Detroit")}
# capitals.pop ("China") #TAKES OUT ITEM YOU DESIRE
# capitals.popitem () #TAKES OUT LATEST ITEM
# keys=capitals.keys ()
# for key in capitals.keys():
#     print (key)

# values =capitals. values ()
# for value in capitals.values():
#     print (values)

# items = capitals.items ()
# for key, value in capitals.items():
#     print (f"{key}: {value}")

# print (capitals)
#if you type an non existent value it gets returned to you=none


#SET
#fruits ={"apple", "banana", "coconut", "kiwi", "blueberry"}
#print(dir(fruits)) #prints out all the methods that come with it
#print(help(fruits))
#print(len(fruits)) 
#print ("apple" in fruits) #True or false of whether something is in there or not
#print (fruits)
#print (fruits[0]) #THIS WILL GIVE YOU AN ERROR WHEN YOU RUN IT IF ITS IN THE CURLY BRACES
#fruits.add ("pineapple") #ADDS ELEMENT
#fruits.remove ("apple") #REMOVES ELEMENT
#fruits.pop() #REMOVES THE LAST ELEMENT
#fruits.clear() #CLEARS ENTIRE THING
#print (fruits)

#for fruit in fruits:
#print(fruit)
# NO INDEX USED IN LIST

#fruits [1] = "pineapple"
#for fruit in fruits:
     #print (fruit)
    # YOU CAN CHANGE VALUES USING THE FUNCTION ABOVE
     
#fruits.append ("pineapple")
#fruits.remove ("apple")
#ruits.index (0,"pineapple")
#fruits.sort()
#fruits.reverse()
#fruits.clear()

#THE TOP SECTION WAS JUST PRACTICE
#cars= ["bwm", "maserati", "audi", "mercedes", "ferrari"]
#print(f"there are a list of {cars}")
#print(f"the first of these cars is {cars[0]}")

#cars [0] = "Toyota"
#print (f"the first of these cars is {cars[0]}")

#print (f"the last cars is {cars[-1]}")
#cars [-1] = "lamborghini"
#print ("the last of these cars is {cars} ")

#cars.append ("Honda")
#print (cars)
#cars.remove ("maserati")
#print (cars)

#for car in cars:
    #print (len(car))
    #print(car)
    #carRequest = input ("add a new car please: ")
    #cars.append(carRequest)
    #print(cars)
    #if len(cars) > 10:
         #break
    #YOU HAVE TO TAB IT OVER FOR IT TO BE CONSIDRED A LOOP


#FRIENDS CHALLENGE
#friends = []
# add a new freind to the list, add at least 5 freinds
#remove one freind from the list
#loop though the list and print the friends name
#if the list is greater than 10 break the loop
#friends.append ("Jenny")
#friends.append ("Vivi")
#friends.append ("hi")
#friends.append ("bye")
#friends.append ("what")
#friends.remove("Vivi")
#for friend in friends:
    #print (len(friend))
    #print (friend)
    #friendRequest= input ("add a new friend please: ")
    #friends.append(friendRequest)
    #if len(friends) > 10:
         #break