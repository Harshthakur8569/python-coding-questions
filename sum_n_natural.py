def natural_no(n):
  if n==0:
    return 0
  else:
    return n + natural_no(n-1)
x=int(input(" enter any no "))  
print(natural_no(x))
  