l1=[1,2,3]
l2=[5,6,7]
l1.append(3)
print(l1)

l1.extend([10,11])
print(11)

print(l1.count(3))
print(l1.count(4))

print(l1.index(2))
print(l1.index(3))

print(l1.pop())
print(l1)

print(l1.pop(2))
print(l1)

l1.remove(10)
print(l1)

l1.reverse()
print(l1)

l1.sort()
print(l1)

l1.insert(1,0)
print(l1)

l1.extend(l2)
print(l1)
