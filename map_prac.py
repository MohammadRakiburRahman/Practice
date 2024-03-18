# Using range() function and no input list
usingrange = {x:x*2 for x in range(12)}
print("Using range(): ",usingrange)

# Lists
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1,2,3,4,5,6,7,8,9,10,11,12]

# Using one input list
numdict = {x:x**2 for x in number}
print("Using one input list to create dict: ", numdict)

# Using two input lists
months_dict = {key:value for (key, value) in zip(number, months)}
print("Using two lists: ", months_dict)

####Set comprehension###
# The set comprehension deals with the set data type and it's very similar to list comprehension. 
# The only key difference is the use of curly brackets for sets instead of square brackets as in lists. For example:
set_a = {x for x in range(10,20) if x not in [12,14,16]}
print(set_a)


####Generator comprehension
#Generator comprehensions are also very similar to lists with the variation of using curved brackets instead of square brackets.
#They are also more memory efficient as compared to list comprehensions. For example:

data = [2,3,5,7,11,13,17,19,23,29,31]
gen_obj = (x for x in data)
print(gen_obj)
print(type(gen_obj))
for items in gen_obj:
    print(items, end = " ")