import random

ls=[random.randint(7500,15000) for i in range(12)]
print(f"Monthly salary {ls} ")
print(f"Average salary per month {round(sum(ls)/12,2)}")