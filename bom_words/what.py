import re

regex = re.compile('(^[a-zA-Z]*)\W([a-zA-Z]+)')
#First parameter is the replacement, second parameter is your input string
r = regex.search('ChristBy')
print(r.group(2))
#Out: 'abdE'
