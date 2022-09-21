def max_end3(nums):
  bigger = nums[0]
  if nums[0] < nums[len(nums) - 1]:
    bigger = nums[len(nums) - 1]



  i = 0

  while i < len(nums):
    nums[i] = bigger
    i += 1



  return nums
