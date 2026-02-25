# PE10 Exercises IB DP Computer Science: Subprograms & Variable Scope

## Objective
In this assignment, we will practice computational thinking by designing **Subprograms** (Functions) in Python. 
Subprograms allow for **modularity** and **abstraction**—key concepts in the IB DP CS syllabus. 

> ⚠️ **GOLDEN RULE:** In these exercises, your subprograms **MUST NOT use `print()`**. You must use the **`return`** keyword to send the value back to the calling process.

## Instructions
1. Open the `PE10exercises.py` file in your IDE.
2. Complete the 9 subprograms by deleting the word `pass` and writing your logic.
3. Run the file (`python PE10exercises.py`) to execute the autotests.

---

## Part 1: Modularity & Subprograms

### Task 1: `format_student_id(name)`
* **Concept:** String manipulation.
* Takes a name and returns an exact string in the format: `"ID-[name]"`. (e.g., `"Ana"` -> `"ID-Ana"`).

### Task 2: `check_parity(number)`
* **Concept:** Data validation and modulo operations.
* Simulates an Even Parity bit check. Return `True` if the number is even, and `False` if it is odd.

### Task 3: `calculate_storage_cost(gb_used, rate_per_gb, tax_percent)`
* **Concept:** Mathematical operations with multiple parameters.
* Calculate the subtotal (`gb_used * rate_per_gb`).
* Calculate the tax (`subtotal * tax_percent / 100`).
* **Return** the final total.

### Task 4: `count_active_flags(binary_stream)`
* **Concept:** Iteration over collections.
* Takes a string of binary data (e.g., `"1011001"`).
* Loop through the string and count how many times the character `"1"` appears. **Return** the count.

### Task 5: `filter_valid_data(data_list)`
* **Concept:** Abstraction (Calling subprograms from within subprograms).
* Loop through the `data_list`.
* **CRITICAL:** Inside your loop, you **must call** your `check_parity(number)` subprogram from Task 2 to check if the current number is even.
* If it is even, append it to a new list. **Return** the new list.

---

## Part 2: Scope & Variable Lifetimes

Variables created *inside* a subprogram or passed as parameters are **local** (they are destroyed when the subprogram ends). Variables created *outside* are **global** (they exist in the main memory space).



### Task 6: `update_system_clock(ticks)` - Global Reassignment
There is a global variable named `system_uptime`. 
* To replace or add to a global integer inside a subprogram, you must explicitly declare `global system_uptime` at the top of your function block.
* Add `ticks` to it, and **return** the new value.

### Task 7: `simulate_local_network()` - Local Shadowing
There is a global variable named `network_mode` set to `"IPv4"`. 
* Do NOT use the `global` keyword.
* Create a local variable named exactly `network_mode` and set it to `"IPv6"`.
* **Return** the local variable. *(This proves that local memory takes priority over global memory without destroying the global state).*

### Task 8: `log_error(error_code)` - Mutable Global Objects
There is a global list named `error_log`.
* In Python, lists are *mutable*. You do **not** need the `global` keyword to append items to a list that already exists.
* Use `.append()` to add `error_code` to the `error_log`.
* **Return** the `error_log`.

### Task 9: `process_data(data_value)` - Parameter Shadowing
There is a global variable named `data_value` set to `100`. Notice that the function's parameter is *also* named `data_value`.
* When a parameter shares a name with a global variable, the parameter "shadows" it. 
* Multiply the parameter `data_value` by 2 and **return** it. *(The test will check that the global 100 was not accidentally changed).*
