# necessary imports
import secrets
import string

# define the alphabet
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars

# password amount
hmdyn = int(input("how many? "))
pwd_length = int(input("length? "))

# generate a password string

while hmdyn != 0:
  pwd = ''
  for i in range(pwd_length):
    pwd += ''.join(secrets.choice(alphabet))

  # generate password meeting constraints
  while True:
    pwd = ''
    for i in range(pwd_length):
      pwd += ''.join(secrets.choice(alphabet))

    if (any(char in special_chars for char in pwd) and
        sum(char in digits for char in pwd)>=2):
            break
  hmdyn -= 1
  print(pwd)

