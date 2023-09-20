# check the factorial number using recursive function
def fact(n):
  if(n==0 or n==1):
    return 1
  else:
    return n*fact(n-1)
n=int(input ("Enter the number : "))
res=fact(n)
print("find the result will be factorial number is :",res)