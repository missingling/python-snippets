# split tuples
tuples = [(1,2), (3,4)]

def split(xy):
    x,y = xy
    return (y,x)

tup = (1,2)
print(split(tup))

# sort tuples
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]

pairs.sort(key = lambda pair: pair[0])
print(pairs)

pairs.sort(key = lambda pair: pair[1])
print(pairs)
