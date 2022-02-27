'''QUESTION 1 '''
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese += 'Oke',
print(cheese)

# expects a collection, since a string is a collection it adds each letter separately to the list
# We can either add square brackets around the string or use a trailing comma

# Add two elements to the list
cheese.extend(['Brie', 'Camembert'])
print(cheese)

'''QUESTION 2 '''
tup = 'Hello'
print(len(tup))
print(type(tup))
# Prints 5, since tup here is a string.
# len(string) returns the number of characters in a string,

tup = 'Hello',
print(len(tup))
print(type(tup))
# Prints 1. Since there is a trailing comma, this is a tuple.
# len(tuple) returns the number of elements in the tuple

