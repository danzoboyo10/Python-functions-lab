# 1) Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n. For example:

def sum_to(n):
  sum_of_ints = 0
  for num in range(n):
    sum_of_ints =  n * (n + 1) // 2
  return sum_of_ints

print(sum_to(6))


# 2) Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

def largest(list):
  max_list_num = list[0]
  for listNum in list:
    if listNum > max_list_num:
      max_list_num = listNum
  return max_list_num
print(largest([8, 11, 6, 2, 1, 9, 10, 3, 12, 7]))

  
# 3) Write a function named occurances that takes two string arguments as input and counts the number of occurances of the second string inside the first string.

def occurances(string1, string2):
  count = 0
  for letter in string1:
    for letters in string2:
      if letter == string2: count += 1
  return count
print(occurances('hello', 'lol'))

  


# 4) Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product.
# (HINT: Review your notes on *args).

def product(*args):
  product_of_nums = 1
  for arg in args:
   product_of_nums = product_of_nums * arg
  return product_of_nums

print(product(3, 5, 2)) 

