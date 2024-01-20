#Pyramid
l = True
while l ==True:
  n=int(input("The rows for the pyramid is?: "))
  i=int(1)
  while n!=0:
    print("*" * i, "\n")
    n-=1
    i+=2
  l=input("wanna play again?(y/n)")
  if l == "y":
    l=bool(1)
  else:
    l=bool(0)


#reverse pyramid
l = True
while l ==True:
  n=int(input("The rows for the pyramid is?: "))
  i=int(1)
  while n!=0:
    print("* "*(2*n - 1))
    n-=1
  l=input("wanna play again?(y/n)")
  if l == "y":
    l=bool(1)
  else:
    l=bool(0)
