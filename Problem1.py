# Instructions: Find the sum of all the
# multiples of 3 0r 5 below 1000.

total = 0

for i in range(1000):
    if (i%3==0) or if(i%5==0):
        total = total + i

Print(total)
