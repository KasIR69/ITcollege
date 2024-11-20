try:
    user_input = int(input("Enter a number: "))
    result = 100 / user_input
    print("Result:", result)
except ValueError:
    print("That's not a number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Operation completed.")

