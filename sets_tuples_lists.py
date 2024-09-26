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
     
#fruits.append ("pineapple")
#fruits.remove ("apple")
#ruits.index (0,"pineapple")
#fruits.sort()
#fruits.reverse()
#fruits.clear()

#THE TOP SECTION WAS JUST PRACTICE
cars= ["bwm", "maserati", "audi", "mercedes", "ferrari"]
print(f"there are a list of {cars}")
print(f"the first of these cars is {cars[0]}")

cars [0] = "Toyota"
print (f"the first of these cars is {cars[0]}")

print (f"the last cars is {cars[-1]}")
cars [-1] = "lamborghini"
print ("the last of these cars is {cars} ")

cars.append ("Honda")
print (cars)
cars.remove ("maserati")
print (cars)

for car in cars:
     #print (len(car))
     #print(car)
    carRequest = input ("add a new car please: ")
    cars.append(carRequest)
    print(cars)
    if len(cars) > 10:
         break
    #YOU HAVE TO TAB IT OVER FOR IT TO BE CONSIDRED A LOOP
    