l=int(input("Input list length "))
import random
ls=[random.randint(0,100) for i in range(l)]
ls2=[ls[i]*2 for i in range(l)]
ls2=ls+ls2
print(ls)
print(ls2)