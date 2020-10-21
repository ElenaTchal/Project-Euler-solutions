# Find the largest palindrome made from the product of two 3-digit numbers.

list1 = range(100,1000)
list2 = range(100,1000)

products_list = [str(i * j) for i in list1 for j in list2]

backwards_list = [z[::-1] for z in products_list]

palindromes = []

for x, y in zip(products_list, backwards_list):
    if x == y:
        x = int(x)
        palindromes.append(x)
palindromes.sort()
print(max(palindromes))
