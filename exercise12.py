# '''QUESTION 1 '''
# cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
# cheese += 'Oke',
# print(cheese)
#
# # expects a collection, as a string is a collection it adds each letter separately to the list
# # We can either add square brackets around the string or use a trailing comma
#
# # Add two elements to the list
# cheese.extend(['Brie', 'Camembert'])
# print(cheese)
#
# '''QUESTION 2 '''
# tup = 'Hello'
# print(len(tup)) # Prints 5, since tup here is a string, a collection
# tup = 'Hello',
# print(len(tup)) # Prints 1

import random
y = []
i=0
while i <5:
    y.append(random.randint(0,5))
    i+=1
print(y)