# Naomi Tesla
# https://codingbat.com/prob/p124676

def near_hundred(n):
  if abs(100 - n) <= 10 or abs(200 - n) <= 10:
    return True
  else:
    return False
