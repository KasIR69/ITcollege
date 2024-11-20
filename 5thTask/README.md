# Знайомство з ООП

## 1. Output of the Program:
When the program is executed, the output is:
```console
>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<
This is object: <__main__.MyName object at 0x000001A6B7E86A50>
This is object attribute: Bohdan / 1
This is <class 'property'>: My name is Bohdan / Bohdan@itcollege.lviv.ua
This is <class 'method'> call: Bohdan@itcollege.lviv.ua
This is static <class 'function'> with defaults: You say: Hello to everyone!
This is class variable <class 'int'>: from class 5 / from object 5
Name length: 6 characters
<*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*>
>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<
This is object: <__main__.MyName object at 0x000001A6B83ACCD0>
This is object attribute: Marta / 2
This is <class 'property'>: My name is Marta / Marta@itcollege.lviv.ua
This is <class 'method'> call: Marta@itcollege.lviv.ua
This is static <class 'function'> with defaults: You say: Hello to everyone!
This is class variable <class 'int'>: from class 5 / from object 5
Name length: 5 characters
<*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*>
>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<
This is object: <__main__.MyName object at 0x000001A6B83ACE10>
This is object attribute: Anonymous / 4
This is <class 'property'>: My name is Anonymous / Anonymous@itcollege.lviv.ua
This is <class 'method'> call: Anonymous@itcollege.lviv.ua
This is static <class 'function'> with defaults: You say: Hello to everyone!
This is class variable <class 'int'>: from class 5 / from object 5
Name length: 9 characters
<*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*>
>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<
This is object: <__main__.MyName object at 0x000001A6B7EFA780>
This is object attribute: Ihor / 5
This is <class 'property'>: My name is Ihor / Ihor@itcollege.lviv.ua
This is <class 'method'> call: Ihor@itcollege.lviv.ua
This is static <class 'function'> with defaults: You say: Hello to everyone!
This is class variable <class 'int'>: from class 5 / from object 5
Name length: 4 characters
<*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*>
We are done. We create 5 names! ??? Why 5?
```

## Answers to the Questions

### 1. Why does an object with the name 'Anonymous' get created when `None` is passed?

When `None` is passed as the argument to the `name` parameter, the `__init__` method checks if the `name` is `None`. If it is, the `anonymous_user()` method is called, which creates an object with the name "Anonymous". This is a fallback mechanism to handle missing names.

### 2. How to change the greeting message when calling the `say_hello()` method?

To change the greeting message, you can modify the default value of the `message` parameter in the `say_hello()` method:

```python
def say_hello(message="Hello from Ihor!"):
    """Static method"""
    return f"You say: {message}"
```
### 3. Add a function in the class to count the number of characters in the name.
To count the number of characters in the name, you can add the following method:

```python
def count_name_length(self):
    """Instance method to count characters in the name"""
    return len(self.name)
```
### 4. Count the number of names in the names list and compare it with the output result.
The names list contains four elements ("Bohdan", "Marta", None, "Ihor"). However, when None is passed, it creates an object with the name "Anonymous", so the total number of objects created is four. The discrepancy arises because None is treated as a special case, resulting in the creation of the "Anonymous" object.
___
## Conclusion

### What was done in the work:
In this task, a class was created with various methods and properties. The class handled input values, including `None`, and displayed behavior based on that. The `say_hello()` method was modified to include a custom greeting, and a new method to count the number of characters in a name was added. The total number of names was compared, highlighting the effect of passing `None`.

### Was the goal achieved:
Yes, the goal of understanding and implementing object-oriented programming concepts, including handling `None` and modifying class methods, was successfully achieved.

### What new knowledge was gained:
The task provided insight into:
- How to handle default values (like `None`) in class constructors.
- How to modify default method parameters.
- How to add custom methods to a class to process data, like counting characters in a name.

### Were all the questions answered during the work:
Yes, all the questions were answered. The behavior of `None` and its impact on object creation was explained, and the method for changing the greeting message was provided. The discrepancy in the name count was clarified as a result of how `None` is handled.

### Were all tasks completed:
Yes, all tasks were successfully completed:
- Created and modified a class.
- Implemented changes to methods as required.
- Answered all questions and provided explanations.

### Were there any difficulties during the task:
No major difficulties were encountered. The task was straightforward, and the concepts were well-understood and applied. The only challenge was ensuring the correct handling of `None` and its effect on object creation.