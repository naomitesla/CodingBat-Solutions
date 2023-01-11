# Naomi Tesla
# https://codingbat.com/prob/p166884

def parrot_trouble(talking, hour):
  if hour < 7 or 20 < hour:
    if talking:
      return True
    else:
      return False
  else:
    return False