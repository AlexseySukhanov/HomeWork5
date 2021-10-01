h=int(input("Input height "))
w=int(input("Input width "))
for i in range(h):
    if i != 0 and i != h - 1:
        st ="*"+" "*(w-2)+"*"
    else:
        st = "*" * w
    print(st)

