#Generate your password. 
import random
chars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*)><?/:;("
length=int(input("Enter length of the password:  "))
password=""

for i in range(length):
  password+=random.choice(chars)
print(password)
#Random is not actually random, rather its based on a "seed value" with the help of which the ranaom works.
