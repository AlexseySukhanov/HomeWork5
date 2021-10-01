dig=int(input("Input digit for multiply table "))
[print(f"{i+1} * {dig} = {(i+1)*dig} ") for i in range(10) if 1<=dig<10]
