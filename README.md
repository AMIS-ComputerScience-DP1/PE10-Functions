#PExercises 10 Python Assignment: Creating and Using Functions

## Objective
In this assignment, we will practice creating **functions** in Python. 
Functions are reusable blocks of code that take inputs (parameters), perform a specific task, and return a result.

> ⚠️ **GOLDEN RULE:** In these exercises, your functions **MUST NOT use `print()`** to show the result. You must use the **`return`** keyword to send the value back. The autotest will check what your function returns, not what it prints.

## Instructions
1. Open the `PE10exercises.py` file in your IDE.
2. Complete the 5 functions by deleting the word `pass` and writing your logic.
3. Run the file (`python PE10exercises.py`) to see if you pass the automatic tests.

---

### Task 1: `greet(name)`
Create a function that takes a name as a parameter and returns a string that says exactly: `"Hello, [name]!"`.
* If it receives `"Ana"`, it must return `"Hello, Ana!"`.

### Task 2: `is_even(number)`
Create a function that checks if an integer number is even.
* Use the modulo operator (`%`).
* If the number is even, the function must **return `True`**.
* If the number is odd, the function must **return `False`**.

### Task 3: `calculate_total(price, quantity, tax_rate)`
Create a function that acts like a cash register.
* First, multiply the `price` by the `quantity` to get the subtotal.
* Next, calculate the tax amount (`subtotal * tax_rate / 100`).
* Add the tax to the subtotal and **return the final total price**.

### Task 4: `count_vowels(text)`
Create a function that analyzes a text string and counts how many vowels it contains in total.
* You will need to use a `for` loop to iterate through each letter of the text.
* Check if the current letter is in `"aeiouAEIOU"`.
* Keep a counter variable and, at the end of the loop, **return the total number** of vowels found.

### Task 5: `filter_even_numbers(numbers_list)`
Create a function that takes a list of numbers and returns a new list containing *only* the even numbers.
* Create an empty list at the start of your function (e.g., `evens = []`).
* Loop through the `numbers_list` using a `for` loop.
* **CRITICAL:** Inside your loop, you **must call** your `is_even(number)` function from Task 2 to check if the current number is even. Do not write `if number % 2 == 0:` again!
* If `is_even()` returns `True`, use `.append()` to add the number to your new list.
* **Return the new list** at the end of the function.
