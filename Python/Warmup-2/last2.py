# Naomi Tesla
# https://codingbat.com/prob/p145834

def last2(str):
  substr = str[len(str)-2:len(str)]
  counter = 0
  for i in range(len(str)-2):
    if str[i] + str[i+1] == substr:
      counter += 1
  return counter
