dim=-2
while not dim%2 or dim<0:
    dim=int(input("Input dimension of hourglass (odd number) "))
s=""
for i in range(dim):
    if i>dim/2:
        i=dim-1-i
    s+=" "*i+"*"*(dim-i*2)
    print(s)
    s=""