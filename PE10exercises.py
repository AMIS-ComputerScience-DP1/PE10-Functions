import sys

# ==============================================================================
#  FUNCTION EXERCISES (Edit these functions)
# ==============================================================================

def greet(name):
    """
    Task 1: Basic function with return
    - Takes a text parameter called 'name'.
    - MUST RETURN (not print) an exact greeting in the format: "Hello, [name]!"
    - Example: if name is "Ana", it returns "Hello, Ana!"
    """
    # TODO: Delete 'pass' and write your code here
    pass

def is_even(number):
    """
    Task 2: Function with booleans and math
    - Takes an integer number.
    - MUST RETURN True if the number is even.
    - MUST RETURN False if the number is odd.
    """
    # TODO: Delete 'pass' and write your code here
    pass

def calculate_total(price, quantity, tax_rate):
    """
    Task 3: Multiple parameters and calculation
    - Takes three numbers: price (float), quantity (int), and tax_rate (float).
    - Calculates the subtotal (price * quantity).
    - Calculates the total by adding the tax percentage to the subtotal.
    - MUST RETURN the final total.
    """
    # TODO: Delete 'pass' and write your code here
    pass

def count_vowels(text):
    """
    Task 4: Functions with loops (Sequences)
    - Takes a string of text.
    - Counts how many vowels (a, e, i, o, u) are in the text.
    - Must count both uppercase and lowercase letters.
    - MUST RETURN the total number of vowels (an integer).
    """
    # TODO: Delete 'pass' and write your code here
    pass

def filter_even_numbers(numbers_list):
    """
    Task 5: Calling a function inside another
    - Takes a list of integers called 'numbers_list'.
    - Creates a new empty list.
    - Loops through 'numbers_list'.
    - MUST CALL your 'is_even(number)' function from Task 2 to check each number.
    - If the number is even, append it to the new list.
    - MUST RETURN the new list containing only the even numbers.
    """
    # TODO: Delete 'pass' and write your code here
    pass


# ==============================================================================
#  TEST RUNNER (Do not modify below this line)
# ==============================================================================
class TestRunner:
    def __init__(self):
        self.failed_checks = 0
        self.total_checks = 0

    def check(self, description, condition, failure_msg):
        self.total_checks += 1
        if condition:
            print(f"  [\033[92mOK\033[0m] {description}")
        else:
            print(f"  [\033[91mFAIL\033[0m] {description}")
            print(f"         -> {failure_msg}")
            self.failed_checks += 1

    def summary(self):
        print("\n" + "="*40)
        print(f"SUMMARY: {self.total_checks - self.failed_checks}/{self.total_checks} Checks Passed")
        print("="*40)
        if self.failed_checks > 0:
            sys.exit(1)

def run_tests():
    t = TestRunner()
    print("\nStarting Function Tests...\n")

    # --- Task 1 ---
    print("--- Checking Task 1: greet() ---")
    try:
        res1 = greet("Ana")
        res2 = greet("Carlos")
        t.check("Returns greeting for Ana", res1 == "Hello, Ana!", f"Expected 'Hello, Ana!', got '{res1}'")
        t.check("Returns greeting for Carlos", res2 == "Hello, Carlos!", f"Expected 'Hello, Carlos!', got '{res2}'")
    except Exception as e:
        print(f"  [CRASH] Task 1 failed with error: {e}")
        t.failed_checks += 1
    print("")

    # --- Task 2 ---
    print("--- Checking Task 2: is_even() ---")
    try:
        t.check("Number 4 is even (True)", is_even(4) is True, f"Expected True for 4, got {is_even(4)}")
        t.check("Number 7 is odd (False)", is_even(7) is False, f"Expected False for 7, got {is_even(7)}")
        t.check("Number 0 is even (True)", is_even(0) is True, f"Expected True for 0, got {is_even(0)}")
    except Exception as e:
        print(f"  [CRASH] Task 2 failed with error: {e}")
        t.failed_checks += 1
    print("")

    # --- Task 3 ---
    print("--- Checking Task 3: calculate_total() ---")
    try:
        res1 = calculate_total(10.0, 2, 21.0)
        res2 = calculate_total(5.0, 4, 10.0)
        
        is_close_1 = False
        if isinstance(res1, (int, float)):
            is_close_1 = abs(res1 - 24.2) < 0.01
            
        is_close_2 = False
        if isinstance(res2, (int, float)):
            is_close_2 = abs(res2 - 22.0) < 0.01

        t.check("Calculation with 21% tax", is_close_1, f"Expected ~24.2, got {res1}")
        t.check("Calculation with 10% tax", is_close_2, f"Expected ~22.0, got {res2}")
    except Exception as e:
        print(f"  [CRASH] Task 3 failed with error: {e}")
        t.failed_checks += 1
    print("")

    # --- Task 4 ---
    print("--- Checking Task 4: count_vowels() ---")
    try:
        res1 = count_vowels("Hello World")
        res2 = count_vowels("Programming")
        res3 = count_vowels("AEIOU")
        res4 = count_vowels("xyz")
        
        t.check("Counts vowels in standard string", res1 == 3, f"Expected 3 vowels in 'Hello World', got {res1}")
        t.check("Counts vowels in longer word", res2 == 3, f"Expected 3, got {res2}")
        t.check("Counts vowels in UPPERCASE", res3 == 5, f"Expected 5, got {res3}")
        t.check("Returns 0 if no vowels", res4 == 0, f"Expected 0, got {res4}")
    except Exception as e:
        print(f"  [CRASH] Task 4 failed with error: {e}")
        t.failed_checks += 1
    print("")

    # --- Task 5 ---
    print("--- Checking Task 5: filter_even_numbers() ---")
    try:
        # Spy on the is_even function to make sure they actually used it
        original_is_even = globals().get('is_even')
        call_count = 0
        def spy_is_even(n):
            nonlocal call_count
            call_count += 1
            return original_is_even(n)
        
        # Replace the function temporarily
        globals()['is_even'] = spy_is_even
        
        res1 = filter_even_numbers([1, 2, 3, 4, 5, 6])
        res2 = filter_even_numbers([7, 9, 11])
        
        # Restore the original function
        globals()['is_even'] = original_is_even

        t.check("Filters even numbers correctly", res1 == [2, 4, 6], f"Expected [2, 4, 6], got {res1}")
        t.check("Returns empty list if no evens", res2 == [], f"Expected [], got {res2}")
        t.check("Calls is_even() inside the loop", call_count > 0, "You didn't call your is_even() function inside Task 5!")
    except Exception as e:
        print(f"  [CRASH] Task 5 failed with error: {e}")
        t.failed_checks += 1

    t.summary()

if __name__ == "__main__":
    run_tests()
