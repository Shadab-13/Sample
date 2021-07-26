import re
zen = """Beautiful is better than ugly.
Explicit is better than implicit idea.
Simple is better than complex.
Sparse is better than dense idea.
Special cases aren't special enough to break the rules.
Although practicality beats purity.!"""

matches = re.findall("beautiful",zen,re.IGNORECASE)
# re.IGNORECASE is an additionl argument given to ignore cases
print(matches)
# "^" is used to find text starting with the word followed by it. 
m = re.findall("^If",zen,re.MULTILINE)
print(m)
# re.MULTILINE is used to find all words in a sentence.
m = re.findall("idea.$",zen,re.MULTILINE)
print(m)

line = "Two too."
m = re.findall("t[ow]o",line,re.IGNORECASE)
print(m)

line = '1233d1sd1? hello'
# \d is used to match digits
m=re.findall("\d",line,re.IGNORECASE)
print(m)

