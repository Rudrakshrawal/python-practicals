import time#represented in time format
clock =time.strftime('%H:%M:%S')#string format time
print(clock)
clock =time.strftime('%H')
print(clock)
clock =time.strftime('%M')
print(clock)
clock =time.strftime('%S')
print(clock)

hour = int(time.strftime('%H'))
print(hour)
if (hour>=0 and hour<12):
  print("Good morning Madam!")
elif (hour>12 and hour>17):
  print("Good afternoon Madam!")
elif(hour>17 and hour<0):
  print("Nighty nightyy!!")
