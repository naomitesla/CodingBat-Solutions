# Naomi Tesla
# https://codingbat.com/prob/p118366

def string_splosion(str):
  cache = ''
  for i in range(len(str)+1):
    cache += str[0:i]
  return cache
