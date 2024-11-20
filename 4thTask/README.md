2024-11-20 01:12:24

# Python Basics 🐍

This document provides a report on the tasks written in Python, explaining the code logic and presenting the output for each program.

---

## 1️⃣ Understanding Data Types

### Code Explanation
The script [`1task.py`](1task.py) demonstrates the creation and use of various data types in Python:
- **String (`str`)**: `name` stores a text value.
- **Integer (`int`)**: `age` represents a whole number.
- **Float (`float`)**: `price` stores a decimal value.
- **List (`list`)**: `fruits` contains an ordered collection of items.
- **Dictionary (`dict`)**: `person` maps keys to values.
- **Tuple (`tuple`)**: `coordinates` is an immutable collection of ordered items.
- **Set (`set`)**: `unique_numbers` holds unordered unique values.

### Program Output
```console
Name: Meow!
Age: 19
Price: 19.99
Fruits: ['apple', 'banana', 'cherry']
Person data: {'name': 'Meow', 'age': 19}
Coordinates: (10, 20)
Unique numbers: {1, 2, 3, 4, 5}
```

## 2️⃣ Constants in Python

### Code Explanation
The script  [`2task.py`](2task.py) demonstrates Python's built-in constants:
- **`None`**: Represents the absence of a value or a null value.
- **`False`**: A boolean constant indicating a false condition.

These constants are essential for controlling program logic and defining states where no value is available.

### Program Output
```console
First constant: None
Second constant: False
```

## 3️⃣ Built-in Functions

The script [`3task.py`](3task.py) demonstrates the use of Python's built-in functions for mathematical operations. The program calculates the absolute value of a number, rounds a floating-point number to one decimal place, and computes the sum of a list of integers.

### Program Output
```console
Absolute value: 50
Rounded number: 2.3
Sum of elements: 15
```

## 4️⃣ Loops in Python

The script [`4task.py`](4task.py) demonstrates the use of loops in Python. It iterates through a list of animals, computes the factorial of a number using a `while` loop, and displays the index and value of colors from a list using a `for` loop.

### Program Output
```console
Animal: cat
Animal: dog
Animal: parrot
Factorial of 5 is 120
Color at position 0 is White
Color at position 1 is Green
Color at position 2 is Red
```

## 5️⃣ Conditional Statements

The script [`5task.py`](5task.py) demonstrates the use of conditional statements in Python. It checks whether a number is even or odd and assigns a grade based on a given score.

### Program Output
```console
The number is even
Grade: Good
```

## 6️⃣ Error Handling

### Code Explanation
The script [`6task.py`](6task.py) demonstrates error handling using `try-except-finally` blocks:
- **`try` Block**: Attempts to perform division, which may raise an exception.
- **`except` Blocks**: Catches and handles specific exceptions:
  - `ValueError`: Raised when the input is not a valid number.
  - `ZeroDivisionError`: Raised when dividing by zero.
- **`finally` Block**: Executes code regardless of whether an exception occurred, ensuring that certain actions (like cleanup) are always performed.

Error handling is crucial for creating robust programs that can gracefully manage unexpected situations.

### Sample Inputs and Outputs

#### Input: `0`
#### Output:
```console
Enter a number: 0
Cannot divide by zero!
Operation completed.
```

#### Input: `69`
#### Output:
```console
Result: 1.4492753623188406
Operation completed.
```

## 7️⃣ Context Managers and File Operations

### Code Explanation
The script [`7task.py`](7task.py) demonstrates the use of context managers for file operations in Python:
- **Writing to a File**: Opens a file in write mode and writes the current timestamp using `time.strftime`.
- **Reading from a File**: Opens the same file in read mode and prints its content.

Context managers (the `with` statement) ensure that resources like files are properly managed, automatically handling tasks such as closing files after their operations are complete.

### Programm output
```console
File content: 2024-11-20 01:12:24
```

## Conclusion

In this task, the following was achieved:

- The implementation of error handling using `try-except-finally` blocks was demonstrated, highlighting how to manage potential exceptions like `ValueError` and `ZeroDivisionError`.
- The use of context managers for file operations was successfully applied, ensuring proper resource management during writing and reading tasks.

### Key Points:
- **Objective Achievement**: The main objectives of the task were successfully completed. Both error handling and file operations using context managers were implemented and tested.
- **New Knowledge**: Gained a deeper understanding of Python's error-handling mechanisms and the importance of context managers in managing file resources.
- **Questions Addressed**: All questions related to error handling and file operations were fully addressed during the work.
- **Tasks Completed**: All assigned tasks were successfully completed without omissions.
- **Difficulties Encountered**: No significant challenges were encountered; the tasks were straightforward and well-structured.
- **Suggestions for Improvement**: It could be beneficial to include optional bonus tasks or challenges to deepen understanding.