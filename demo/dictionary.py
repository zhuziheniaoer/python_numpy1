# 字典
d = {'cat': 'cute', 'dog': 'furry'}
print(d['cat'])  # cute
print('cat' in d)  # True check if a dictionary has a given key
d['fish'] = 'wet'
print(d['fish'])   # wet
print(d.get('monkey', 'N/A'))  # get an element with a default
print(d.get('fish', 'N/A'))
del d['fish']  # remove an element from a dictionary
print(d)

# loop
d2 = {'person': 2, 'cat': 4, 'spider': 8}
for animal in d2:
    legs = d2[animal]
    print('A %s has %d legs' % (animal, legs))

for animal, items in d2.items():
    print('A %s has %d legs' % (animal, items))


# 字典生成式 dictionary comprehensions
nums = [0, 1, 2, 3, 4]
num_to_square = {x: x ** 2 for x in nums}
print(num_to_square)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

even_num_to_square = {x: x ** 3 for x in nums if x % 2 == 0}
print(even_num_to_square)  # {0: 0, 2: 8, 4: 64}
