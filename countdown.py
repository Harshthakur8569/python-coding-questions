def countdown():
    global n  # Using a global variable to track the count
    if n == 0:  # Base case
        print("Done!")
    else:
        print(n)
        n -= 1  # Decrement the count
        countdown()  # Recursive call

# Initialize the global variable
n =int(input(" enter value"))
countdown()