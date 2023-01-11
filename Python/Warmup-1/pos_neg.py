# Naomi Tesla
# https://codingbat.com/prob/p162058

def pos_neg(a, b, negative):
  if (a + abs(a) == 0) and (b + abs(b) == 0):
    if negative:
      return True
    else:
      return False
  elif (a + abs(a) == 0) or (b + abs(b) == 0):
    if negative:
      return False
    else:
      return True
  else:
    return False
