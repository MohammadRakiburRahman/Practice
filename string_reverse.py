# str[start: stop: step]  slice funtion 

trail = "reversal"
new_trail = trail[::-1]
print(f"using slice ->" + new_trail)


# Using recurssion


def str_rev(str):
    if len (str)==0:
        return str
    else:
        return str_rev(str[1:])+str[0]
    
str = "reversal"
reverse = str_rev(str)
print("using reccursive -> " + reverse)