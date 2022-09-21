def rotate_left3(nums):
  i = 1
  list = []
  last = nums[0]
  while i < len(nums):
    if i == len(nums) - 1:
      list.append(nums[i])
    elif i != 0:
      list.append(nums[i])

    i += 1
  list.append(last)
  return list
