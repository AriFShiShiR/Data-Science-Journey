color =["red","green","blue"]
print(color)
color[1] = "yellow"
color.append("purple")
color.remove("red")
print(color)

#list comprehension.
new_color =[nlist for nlist in color if 'u' in nlist]
print(new_color)

# Method 	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
