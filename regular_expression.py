
import re

# To returns a match object
word = 'My Name is Toludoyin. A Machine learner'
x = re.search('learner', word)
if x:
    print('Right!')
else:
    print('Try again')


# To findall, returns a list containing all matches
word = 'My Name is Toludoyin. A Data Scientist'
x =re.findall('is', word)
print(x)


# metacharacters:
# ^ = startwith
# $ = endswith
# () = capture the group
# | = either or
# {} = exactly the specify number of occurence
# [] = set of characters
# * = zero or more occurence
# + = one or more occurence
# . = any character