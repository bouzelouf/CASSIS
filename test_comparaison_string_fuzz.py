from fuzzywuzzy import fuzz



str1 = input("choisissez une phrase : ")
str2 = input("choisissez une autre phrase : ")

a = fuzz.ratio(str1, str2)

b = fuzz.partial_ratio(str1, str2)
# 100
print (a,b)

c = fuzz.token_sort_ratio('Barack Obama', 'Barack H. Obama')
# 92
d = fuzz.token_set_ratio('Barack Obama', 'Barack H. Obama')
# 100
print (c,d)
'''
fuzz.token_sort_ratio('Barack H Obama', 'Barack H. Obama')
# 100
fuzz.token_set_ratio('Barack H Obama', 'Barack H. Obama')
# 100

query = 'Barack Obama'
choices = ['Barack H Obama', 'Barack H. Obama', 'B. Obama']
# Get a list of matches ordered by score, default limit to 5
process.extract(query, choices)
# [('Barack H Obama', 95), ('Barack H. Obama', 95), ('B. Obama', 85)]

# If we want only the top one
process.extractOne(query, choices)
# ('Barack H Obama', 95)
'''
