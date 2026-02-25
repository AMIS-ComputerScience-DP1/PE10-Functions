import sys

# ==============================================================================
#  IB DP CS: MODULARITY & SUBPROGRAMS (Edit these functions)
# ==============================================================================

def format_student_id(name):
    """
    Task 1: Basic Subprogram (String Manipulation)
    - Takes a text parameter 'name'.
    - MUST RETURN an exact ID string in the format: "ID-[name]"
    - Example: if name is "Ana", it returns "ID-Ana"
    """
    # TODO: Delete 'pass' and write your code here
    pass

def check_parity(number):
    """
    Task 2: Data Validation (Booleans & Modulo)
    - Simulates an Even Parity check.
    - Takes an integer 'number'.
    - MUST RETURN True if the number is even.
    - MUST RETURN False if the number is odd.
    """
    # TODO: Delete 'pass' and write your code here
    pass

def calculate_storage_cost(gb_used, rate_per_gb, tax_percent):
    """
    Task 3: Computational Thinking (Mathematical Operations)
    - Calculates the cost of cloud storage.
    - Subtotal = gb_used * rate_per_gb.
    - Tax = subtotal * tax_percent / 100.
    - MUST RETURN the final total (subtotal + tax).
    """
    # TODO: Delete 'pass' and write your code here
    pass

def count_active_flags(binary_stream):
    """
    Task 4: Iteration over Collections (Sequences)
    - Takes a string of binary data (e.g., "1011001").
    - Counts how many times the character "1" appears in the stream.
    - MUST RETURN the total count (an integer).
    """
    # TODO: Delete 'pass' and write your code here
    pass

def filter_valid_data(data_list):
    """
    Task 5: Abstraction (Calling Subprograms)
    - Takes a list of integers.
    - Creates a new empty list.
    - MUST CALL your 'check_parity(number)' subprogram from Task 2 inside a loop.
    - If check_parity returns True, append the number to the new list.
    - MUST RETURN the new list containing only the even numbers.
    """
    # TODO: Delete 'pass' and write your code here
    pass


# ==============================================================================
#  IB DP CS: VARIABLE SCOPE & LIFETIME
# ==============================================================================

# Global Variable for Task 6
system_uptime = 0

def update_system_clock(ticks):
    """
    Task 6: Global Scope (Reassignment)
    - Modifies the global variable 'system_uptime'.
    - Use the 'global' keyword to update it.
    - Add 'ticks' to 'system_uptime'.
    - MUST RETURN the new 'system_uptime'.
    """
    # TODO: Delete 'pass' and write your code here
    pass


# Global Variable for Task 7
network_mode = "IPv4"

def simulate_local_network():
    """
    Task 7: Local Scope (Shadowing)
    - Do NOT use the 'global' keyword.
    - Create a LOCAL variable named 'network_mode'.
    - Set your local 'network_mode' to "IPv6".
    - MUST RETURN your local 'network_mode'.
    """
    # TODO: Delete 'pass' and write your code here
    pass


# Global Variable for Task 8
error_log = []

def log_error(error_code):
    """
    Task 8: Global Scope (Mutable Objects)
    - Modifies the global list 'error_log'.
    - Unlike integers/strings, you don't need the 'global' keyword to append to a list.
    - Append the 'error_code' parameter to the 'error_log' list.
    - MUST RETURN the updated 'error_log' list.
    """
    # TODO: Delete 'pass' and write your code here
    pass


# Global Variable for Task 9
data_value = 100

def process_data(data_value):
    """
    Task 9: Parameter Shadowing
    - The parameter 'data_value' shares a name with the global variable.
    - Multiply the PARAMETER 'data_value' by 2.
    - MUST RETURN the modified parameter.
    - (The autotest will verify that the global data_value remained 100).
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
    print("\nStarting IB DP CS Subprograms & Scope Tests...\n")

    print("--- Task 1: format_student_id() ---")
    try:
        t.check("Formats Ana's ID", format_student_id("Ana") == "ID-Ana", "Expected 'ID-Ana'")
    except Exception as e: print(f"  [CRASH] {e}"); t.failed_checks += 1

    print("\n--- Task 2: check_parity() ---")
    try:
        t.check("Even parity logic (True)", check_parity(4) is True, "Expected True for 4")
        t.check("Even parity logic (False)", check_parity(7) is False, "Expected False for 7")
    except Exception as e: print(f"  [CRASH] {e}"); t.failed_checks += 1

    print("\n--- Task 3: calculate_storage_cost() ---")
    try:
        res = calculate_storage_cost(10.0, 2, 21.0)
        is_close = isinstance(res, (int, float)) and abs(res - 24.2) < 0.01
        t.check("Calculates cost with 21% tax", is_close, f"Expected ~24.2, got {res}")
    except Exception as e: print(f"  [CRASH] {e}"); t.failed_checks += 1

    print("\n--- Task 4: count_active_flags() ---")
    try:
        t.check("Counts '1's in binary stream", count_active_flags("1011001") == 4, "Expected 4")
    except Exception as e: print(f"  [CRASH] {e}"); t.failed_checks += 1

    print("\n--- Task 5: filter_valid_data() ---")
    try:
        original_parity = globals().get('check_parity')
        call_count = 0
        def spy_parity(n):
            nonlocal call_count; call_count += 1; return original_parity(n)
        globals()['check_parity'] = spy_parity
        res1 = filter_valid_data([1, 2, 3, 4, 5, 6])
        globals()['check_parity'] = original_parity
        t.check("Filters correctly", res1 == [2, 4, 6], f"Expected [2, 4, 6], got {res1}")
        t.check("Calls check_parity()", call_count > 0, "You didn't call check_parity() inside Task 5!")
    except Exception as e: print(f"  [CRASH] {e}"); t.failed_checks += 1

    print("\n--- Task 6: update_system_clock() (Global Reassignment) ---")
    try:
        global system_uptime; system_uptime = 0
        res = update_system_clock(15)
        t.check("Modifies global variable", system_uptime == 15, "Did you use the 'global' keyword?")
    except Exception as e: print(f"  [CRASH] {e}"); t.failed_checks += 1

    print("\n--- Task 7: simulate_local_network() (Local Shadowing) ---")
    try:
        global network_mode; network_mode = "IPv4"
        res = simulate_local_network()
        t.check("Returns local variable", res == "IPv6", f"Expected 'IPv6', got {res}")
        t.check("Global remains unchanged", network_mode == "IPv4", "You overwrote the global variable!")
    except Exception as e: print(f"  [CRASH] {e}"); t.failed_checks += 1

    print("\n--- Task 8: log_error() (Mutable Global) ---")
    try:
        global error_log; error_log = []
        res = log_error("ERR_404")
        t.check("Appends to global list", error_log == ["ERR_404"], "Did not append to error_log.")
    except Exception as e: print(f"  [CRASH] {e}"); t.failed_checks += 1

    print("\n--- Task 9: process_data() (Parameter Shadowing) ---")
    try:
        global data_value; data_value = 100
        res = process_data(50)
        t.check("Modifies parameter correctly", res == 100, f"Expected 100, got {res}")
        t.check("Global remains unchanged", data_value == 100, f"Global variable changed to {data_value}!")
    except Exception as e: print(f"  [CRASH] {e}"); t.failed_checks += 1

    t.summary()

if __name__ == "__main__":
    import sys
    run_tests()
