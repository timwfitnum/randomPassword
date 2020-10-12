import random

__name__ = "__main__"

def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

def rndmChar():
  rndm = random.randint(0, 9)
  if  rndm >= 3:
    return chr(random.randint(48, 57))
  elif rndm <= 7 and rndm > 3:
    return chr(random.randint(97, 122))
  else:
    return chr(random.randint(65, 90))


def main():
  input_var = input("Enter password length:")
  length = int(input_var)
  password = ""
  password+=chr(random.randint(65,90))
  password +=chr(random.randint(97, 122))
  password+=chr(random.randint(48, 57))
  for i in range(length-3):
    password += rndmChar()
  
  password = shuffle(password)
  print("\n" + password)
  

if __name__ == "__main__":
  main()

