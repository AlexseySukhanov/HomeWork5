num=int(input("Input a number "))
fac=1
if 4 < num < 16:
    for i in range(2,num+1):
        fac*=i
print(fac)
