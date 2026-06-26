# mysets = set('hello')
# print(mysets)

myset = set()

myset.add(1)
myset.add(2)
myset.add(3)

# myset.remove(4)
# myset.discard(5)

# print(myset.pop())
# print(myset)

# for x in myset:
#     print(x)

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

# union = odds.union(evens)
# print(union)

# intersection = odds.intersection(primes)
# print(intersection)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff = setA.difference(setB)
# print(diff)
diff = setB.difference(setA)
# print(diff)
diff2 = setA.symmetric_difference(setB)
# print(diff2)

both = setA.intersection(setB)
# print(both)

setA.update(setB)
# print(setA)

m =set(setA | setB)
# print(m)


setB = {1, 2, 3, 10, 11, 12}
setA = {1, 2, 3}
setC = {7, 8}

# print(setA.issubset(setB))

# print(setA.issuperset(setB))

# print(setB.issuperset(setA)) 

print(setC.isdisjoint(setB))