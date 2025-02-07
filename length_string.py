def sting_length(n):
  if n=="": # empty string
    return 0
  else:
    return 1+sting_length(n[1:])
n=input()
print(sting_length(n))  
  

