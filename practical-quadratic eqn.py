#FIND ROOTS OF QUADRATIC EQUATIONS)
def eqn(a,b,c):
  global det
  det= b**2-4*a*c
  if det>0 or det==0:
    x1=(-b+(det)**0.5)/2*a*c
    x2=(-b-(det)**0.5)/2*a*c
    return x1,x2
  elif det<0:
    return "No real Solution"

l=True
while l==True:
  a=int(input("Write the coefficient of x^2:  "))
  b=int(input("Write the coefficient of x:  "))
  c=int(input("Write the independent coefficient:  "))
  print(eqn(a,b,c))
  l=input("Do you want to find another solution? :(y/n)")
  if l=="y":
     l=bool(1)
  else :
     l=bool(0)

  
