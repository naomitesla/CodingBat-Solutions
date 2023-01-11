# Naomi Tesla
# https://codingbat.com/prob/p129981

def make_out_word(out, word):
  first = out[0:2]
  last = out[2:4]
  return "{0}{1}{2}".format(first, word, last)
