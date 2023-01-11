# Naomi Tesla
# https://codingbat.com/prob/p149524

def missing_char(str, n):
  if n > 0:
    return str[0:n] + str[n+1:len(str)]
  else:
    return str[1:len(str)]
