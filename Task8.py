dim=input("Input square matrix dimension (4 - default) ")
prn=input("Print matrix in square or row(s/r, square - default) ")
if not prn:
    prn="s"
if not dim:
    dim=4
else:
    dim=int(dim)
ls=[]
ls_inner=[]
s=0
for i in range(dim):
    ls_inner+=([(i*dim+j+1) for j in range(dim)])
    s+=sum(ls_inner)
    ls.append(ls_inner)
    if prn.lower()=="s":
        print(ls_inner)
    ls_inner=[]
if prn.lower()=="r":
    print(ls)
print(f"Sum of all elemets of matrix {s}")
