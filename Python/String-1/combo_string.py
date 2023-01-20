# Naomi Tesla
# https://codingbat.com/prob/p194053

def combo_string(a, b):
  if len(a) > len(b):
    return b + a + b
  return a + b + a
