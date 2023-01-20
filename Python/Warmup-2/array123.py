# Naomi Tesla
# https://codingbat.com/prob/p193604

def array123(nums):
  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False



""" 

My original code was the following implementing a FILO data structure,
my initial idea was the actual solution but I thought it'd be fun
to implement; however, it was ulitmately about a microsecond slower on
average so I ultimately chose to go with the more efficient implementation.


def array123(nums):
    ref = [1, 2, 3]
    cache = [0, 0, 0]
    for i in range(0, len(nums)):
        cache.append(nums[i])
        cache.pop(0)
        if cache == ref:
            return True
    return False

"""
