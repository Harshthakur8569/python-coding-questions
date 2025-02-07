# def recursive_factorial(n):
#   if n == 1:
#       return n
#   else:
#       return n * recursive_factorial(n-1)

# # user input
# num = 6

# print("Factorial of number", num, "=", recursive_factorial(num))




def recursive_fibonacci(n):
    
  if n <= 1:
      return n
  else:
      return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))

n_terms = 10

print(recursive_fibonacci(n_terms))