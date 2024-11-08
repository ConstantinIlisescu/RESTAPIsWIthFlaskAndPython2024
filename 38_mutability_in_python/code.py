a = []
b = a

## prints the location id in memory (they have the same id)
print(id(a))
print(id(b))

a.append(35)

## both chnaged to 35
print(a)
print(b)

## all items are muttable unless they are imuttable items like :

c = () ## immutable touple
c = c + (15,) ## is going to create a new itme not modify the existing one


d = 111
e = 111

## they will have the same location in memory (python has this optimisation where the same integer is not created twice)
print(id(a))
print(id(b))

