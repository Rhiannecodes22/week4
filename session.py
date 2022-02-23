# first_name = 'first'
# last_name = 'last'
# print(first_name,last_name, sep='@@')
#
# list1 = [1, 2, 3, 'four']
# print(list1, first_name, sep='?')
#
# '''look up reduce'''
#
# '''collections'''
# #ORDERED
# strings = 'norwegian blue'
# a_list = ['yes', 'no', 'maybe']
# a_tuple = ('yes', 'no', 'maybe')
# #UNORDERED
# set = {1: 'yes', 2: 'no', 3:'maybe'}
#
# my_list = [2, "first", ['apples','oranges'], 9.8]
# print(my_list[0])
# print(my_list[-1])
# print('i have {} elements in my list'.format(len(my_list)))
# print(my_list[2][1])
# for elements in my_list:
#     print('list items {}:', elements)
# yes = 'yesplease'
# print(min(yes))
## print(min(my_list)) this would return an error as we are comparing a list with s string

# my_tuple = ('yes', 9, ('tuple', 'inside', 'a', 'tuple'))
# print(my_tuple[-1])
# print(len(my_tuple))
# # parenthesis are not necessary. you have multiple variables separated by commas
# a=9
# b=8
# print(a,b)
# tmp = a
# a=b
# b=tmp
# print(a,b)
# a, b = b, a # same as a, b = (b, a)
# #unpacking
# var1, *var2= my_tuple #*forms a list with leftover elements
# print(var1)
# print(var2)
# # print(var3)
#
# new_tuple = ('yes', 'no', 'maybe', 9,9,9, ('tuple', 'inside', 'a', 'tuple'))
# print(len(new_tuple))
#
# var1, var2, *var3, var4 = new_tuple
# print('var1',var1)
# print('var2',var2)
# print('var3',var3)
# print('var4',var4)
#
# # creating a tuple with one element
# # we need the trailing comma
# thing = 'hello'
# print(type(thing))
#
# thing = 'hello',
# print(type(thing))

'''PYTHON LISTS'''
#
# my_shopping_list = ['apples', 'oranges', 'milk']
#
# # add elements to the beginning of the list
# my_shopping_list[:0] = ['bread', 'eggs']
# print(my_shopping_list)
#
# my_shopping_list[:0] = ['tomatoes']
# print(my_shopping_list)
#
# my_shopping_list[:0] = ('biscuits',)
# print(my_shopping_list)
#
# # add elements to the end of string
# my_shopping_list += ('chocolate',)
# print(my_shopping_list)
# my_shopping_list += ('chocolate', 'flowers')
# print(my_shopping_list)
#
# my_shopping_list.append('muesli')
# print(my_shopping_list)
#
# # my_shopping_list.append(['muesli', 'cereal'])
# # print(my_shopping_list)
# my_shopping_list.extend(['muesli', 'cereal'])
# print(my_shopping_list)
#
# # specific position
# my_shopping_list.insert(3, 'bananas') # everything was shifted
# print(my_shopping_list)
#
# del my_shopping_list[3:5]
#
# my_shopping_list.pop()
# print(my_shopping_list)
# returned_element = my_shopping_list.pop(9)
# print(returned_element)
#
# my_shopping_list.remove('milk')
# # returned_element = my_shopping_list.remove('milk')
# print(my_shopping_list)
#
# my_shopping_list.sort(key=len)
# print('sorted list:', my_shopping_list)

# nums = ['1001', '34', '3', '77', '42', '9', '87']
# newstr = sorted(nums)
# newnum = sorted(nums, key=int)
# print(newstr)
# print(newnum)

'''SETS'''
# sets are mutable, items must be
myset = {100, 2, 578, 89, 2, 2, 2, 646, 9, 27}
myset.discard(2)

print(myset)
# to remove duplicates from a list, turn into a set and then back into a list
