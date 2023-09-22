import random

# Roll 3d6 six times and print the results
for i in range(6):
    roll = sum(random.randint(1, 6) for _ in range(3))
    print(roll)
