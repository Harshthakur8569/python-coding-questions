def countdown(n):
    if n == 0:  # Base case
        print("Done!")
    else:
        print(n)
        countdown(n - 1)  # Recursive call with a decremented value

# Example usage:
countdown(5)