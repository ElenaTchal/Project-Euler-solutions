# What is the largest prime factor of the number 600851475143?

def find_prime_facs(n):
  list_of_factors=[]
  i=2
  while n>1:
    if n%i==0:
      list_of_factors.append(i)
      n=n/i
      i=i-1
    i+=1
  return list_of_factors
print (max(find_prime_facs(600851475143)))
