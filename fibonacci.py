def fibonacci(n):
  if n<=1:
    return 1
  else :
    return (n-1)+(fibonacci(n-2))

n=int(input(" enter the value ")) 
print(fibonacci(n) )