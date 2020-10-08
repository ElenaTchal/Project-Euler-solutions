#Instructions: add up all the even Fibonacci numbers not exceeding 4 million

#Note: Instead of adding all the Fibonacci numbers to a list,
# (because not enough memory for that), I kept a running sum.

totalsum = 2

m1 = 1
m2 = 2
while m1<4000000:
    m3 = m1 + m2
    if m3 % 2 == 0:
        totalsum = totalsum + m3
    m1 = m2
    m2 = m3
    if m3>=4000000:
        break
print(totalsum)
