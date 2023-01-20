# Naomi Tesla
# https://codingbat.com/prob/p113152

def string_bits(str):
  result = ""
  for i in range(len(str)):
    if not i%2:
      result = result + str[i]
  return result
