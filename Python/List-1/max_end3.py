# Naomi Tesla
# https://codingbat.com/prob/p135290

def max_end3(nums):
  if nums[0] > nums[len(nums)-1]:
    return [nums[0]]*3
  return [nums[len(nums)-1]]*3
