# # list operations
# cars = ['BMW' , 'Nano', 'Swift','Alto-800']
# print (cars[0])
# print (cars[-2])
# print(cars[-1])

# #modify list items
# cars[1] ="Benz"

# print(cars)
# Print the entire list
# print(cars)

# #append = adds the element
# cars.append("Volvo")
# print(cars)

# #insert
# cars.insert(2,"audi01")
# print(cars)

# #remove - remove first occurence
# cars.remove("Volvo")

# #pop -- default remove it's last 
# cars.pop()
# print(cars)

# #pop
# cars.pop(2)
# print(cars)


# #index
# print(cars.index("BMW"))
# print(cars.index("Benz"))


# #extend -- adds element from anothher list
# a =[1,2,3,4]
# b = [5,6,7,8]
# a.extend(b)
# print(a)


# #clear = removes all the elements
# cars.clear()
# print(cars)



fruits = ['apple','banana','apple','cherry']
#count -- count the how many times item is appear
print(fruits.count("apple"))
print(fruits.count("cherry"))




print(len(fruits))



#sort
fruits.sort()#sort the list in ascending order
print(fruits)
fruit.reverse()
print(fruits)
#copy-return the copy of list
new_fruits = fruits.copy()
print(new_fruits)


#list slicing
fruit1 = ['apple','banana','cherry' , 'mango']
print(fruits[1:4])