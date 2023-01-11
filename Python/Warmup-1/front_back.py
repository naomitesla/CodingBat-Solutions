# Naomi Tesla
# https://codingbat.com/prob/p153599

def front_back(str):
  if len(str) > 1:
    return str[len(str)-1:len(str)] + str[1:len(str)-1] + str[0:1]
  else:
    return str
