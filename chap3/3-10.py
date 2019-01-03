# Every function

categories = ['country', 'city', 'plant', 'animal', 'object', 'boy name',
                'girl name', 'famous person']
print(categories[-7].title())
categories.append('foo')
categories.pop()
categories.insert(0,"bar")
del categories[0]
categories.remove('famous person')
categories.sort()
print(categories)
categories.sort(reverse=True)
print(categories)
print(sorted(categories))
categories.reverse()
print(categories)
print(len(categories))