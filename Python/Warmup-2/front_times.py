# Naomi Tesla
# https://codingbat.com/prob/p165097

def front_times(str, n):
  if len(str) >= 3:
    return str[0:3]*n
  else:
    return str*n
