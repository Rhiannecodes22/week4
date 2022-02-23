cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese += ['Oke'] # #expects a collection, as a string is a collection it adds each letter separately to the list
# square brackets were missing
print(cheese)
cheese.append('oke') # append can only be used for one element
print(cheese)
cheese.extend(['Brie','Camembert'])
print(cheese)

tup = 'Hello'
print(len(tup))
tup = 'Hello',
print(len(tup)) # here tip
