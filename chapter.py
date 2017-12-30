# Take each of the data items in the original lists, sanitize them,
# and then append the sanitized data to the appropriate new list.
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)

    (mins, secs) = time_string.split(splitter)

    return (mins + '.' + secs)

# The code that reads the data from the data files remains unchanged
with open('james.txt') as jaf:
    data = jaf.readline()
james = data.strip().split(',')

with open('julie.txt') as juf:
    data = juf.readline()
julie = data.strip().split(',')

with open('mikey.txt') as mif:
    data = mif.readline()
mikey = data.strip().split(',')

with open('sarah.txt') as saf:
    data = saf.readline()
sarah = data.strip().split(',')
# same operations we can do, using list comprehension (line 74,75,76)
# create four new, initially empty lists.
clean_james = []
clean_julie = []
clean_mikey = []
clean_sarah = []

for each_t in james:
    clean_james.append(sanitize(each_t))
for each_t in julie:
    clean_julie.append(sanitize(each_t))
for each_t in mikey:
    clean_mikey.append(sanitize(each_t))
for each_t in sarah:
    clean_sarah.append(sanitize(each_t))

# four 'print()' statements now display the new lists, which are sorted too.
print(sorted(clean_james))
print(sorted(clean_julie))
print(sorted(clean_mikey))
print(sorted(clean_sarah))

# Its's never been so easy to turn something dirty into something clean.
dirty = ['2-22','2:33','2.44']
clean = [sanitize(t) for t in dirty]
# output ['2.22', '2.33', '2.44']
print(clean)


# The 'float()' BIF converts to floating point.
dirty = ['2.22','3.33','4.44']
clean = [float(s) for s in dirty]
# output [2.22, 3.33, 4.44]
print(clean)

# function chains read from right to left
# Combining transformations on the data items is supported, too!!
dirty = ['2-22','2:33','2.44']
clean = [float(sanitize(t)) for t in dirty]
# output [2.22, 2.33, 2.44]
print(clean)


# list comprehension (without list comprehension you can get same output in line 33-51 )
print(sorted([sanitize(each_t) for each_t in james]))
print(sorted([sanitize(each_t) for each_t in julie]))
print(sorted([sanitize(each_t) for each_t in mikey]))
