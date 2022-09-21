def reverse3(nums):
  i = len(nums)
  list = []

  while i > 0:
    list.append(nums[i - 1])
    i -= 1
  return list
