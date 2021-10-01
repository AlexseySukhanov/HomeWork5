simple=True
for i in range(2,101):
    for j in range(2,i):
        if not i%j and i!=j: simple=False
    if simple:
        print(i)
    simple=True
