def fibonacci():
    a, b = 0, 1
    while True:
        print(f"Current Fibonacci number: {a}")
        a, b = b, a + b
        
        # Check for spacebar press
        user_input = input("Press spacebar and Enter to stop, or just Enter to continue: ")
        if user_input == " ":
            break

print("Welcome to Fibonacci sequence generator!")
print("Press Enter to see next number or spacebar + Enter to stop")


fibonacci()
