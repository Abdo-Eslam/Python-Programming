items = ["bannana" , "apple" , "orange" , "grape" , "kiwi" , "mango" , "pear" , "peach" , "plum" , "cherry"]
items_num = [1, 6, 7, 9, -3, -5, 4]
index = items[0]
print(index)


for x in items:
    print(x)


if "bannana" in items:
    print("Yes, bannnana is in the list")
else:
    print("No, bannana is not in the list")    



print(len(items))

add = items.append("watermalon")
print(items)

items.insert(0, "house")

print(items)


list = items.pop(0)
# list = items[-1]
print(list)
print(items)

items.remove("orange")
print(items)

items.clear()
print(items)

items.reverse()
print(items)


items_num.sort()
print(items_num)
number = sorted(items_num)
print(number)


number = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(number[1:])

print(number[1:-1])

print(number[1::])

print(number)
loop = [x*x for x in number]
print(loop)


