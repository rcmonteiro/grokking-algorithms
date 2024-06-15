def binary_search(list, item):
  low = 0
  high = len(list) - 1

  while low <= high:
    middle = (low + high) // 2
    guess = list[middle]

    if guess == item:
      return middle
    if guess > item:
      high = middle - 1
    else:
      low = middle + 1

  return None

sample_list = [1, 3, 4, 5, 7, 9]

print(binary_search(sample_list, 3))
print(binary_search(sample_list, -1))

# In a given sorted list with 128 names, what is the maximum number of steps 
# to find a name using binary search?
# >>> log(n) = log(128) = 7 steps
# If we double the size of the list, what is the maximum number of steps?
# >>> log(n) = log(256) = 8 steps
# Just one more step is needed to find the name.

# Talking about execution time, in a given list with 100 names, 
# we'll need 100 steps, this is a linear search, using linear time execution.
# In a list with 4 billion names, we'll need 4 billion steps, but using
# binary search we'll need only 32 steps, this is a logarithmic time execution.