# 1. Aktualizowanie dicto-ow

d1 = {'a': 100, 'b': 200}
d2 = {'b': 300, 'c': 400}

# d1.update(d2)
# print(d1)

# d11 = d1.copy()
# d11.update(d2)
# print(d1)
# print(d11)

d3 = d1 | d2
print(d1)
print(d2)
print(d3)

# d1 |= d2
print(d1)

d3 = {**d1, **d2}
print(d3)

# Operator | wymaga po dwoch stronach dict
d1 |= [('b', 300), ('c', 400)]
print(d1)

# Operator | oraz |= moze pracowac rowniez z:
# defaultdict, ChainMap, OrderedDict, UserDict,
# WeakKeyDictionary, WeakValueDictionary i jeszcze
# kilkoma innymi