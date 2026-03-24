def display_ascending(limit_val):
    if limit_val > 0:
        display_ascending(limit_val - 1)
        print(limit_val, end=" ")


def display_descending(start_val):
    if start_val > 0:
        print(start_val, end=" ")
        display_descending(start_val - 1)


def sum_natural_recursive(val):
    if val <= 0:
        return 0
    return val + sum_natural_recursive(val - 1)


def calculate_factorial(num):
    if num <= 1:
        return 1
    return num * calculate_factorial(num - 1)


def compute_power(base_val, exponent_val):
    if exponent_val == 0:
        return 1
    return base_val * compute_power(base_val, exponent_val - 1)


def sum_of_digits_recursive(number):
    if number == 0:
        return 0
    return (number % 10) + sum_of_digits_recursive(number // 10)


def count_digits_recursive(number):
    if number < 10:
        return 1
    return 1 + count_digits_recursive(number // 10)


def reverse_integer(number, current_reversed=0):
    if number == 0:
        return current_reversed
    new_reversed = current_reversed * 10 + (number % 10)
    return reverse_integer(number // 10, new_reversed)


def get_nth_fibonacci(index):
    if index == 0:
        return 0
    elif index == 1:
        return 1
    return get_nth_fibonacci(index - 1) + get_nth_fibonacci(index - 2)


def is_text_palindrome(text):
    if len(text) <= 1:
        return "Palindrome"
    if text[0] != text[-1]:
        return "Not palindrome"
    return is_text_palindrome(text[1:-1])


def sum_of_sequence(num_sequence):
    if not num_sequence:
        return 0
    return num_sequence[0] + sum_of_sequence(num_sequence[1:])


def find_max_recursive(num_sequence):
    if len(num_sequence) == 1:
        return num_sequence[0]
    max_in_rest = find_max_recursive(num_sequence[1:])
    return num_sequence[0] if num_sequence[0] > max_in_rest else max_in_rest


def count_target_occurrences(num_sequence, target_val):
    if not num_sequence:
        return 0
    match_found = 1 if num_sequence[0] == target_val else 0
    return match_found + count_target_occurrences(num_sequence[1:], target_val)


def linear_search_recursive(num_sequence, target_val):
    if not num_sequence:
        return "Not Found"
    if num_sequence[0] == target_val:
        return "Found"
    return linear_search_recursive(num_sequence[1:], target_val)


def check_if_sorted_asc(num_sequence):
    if len(num_sequence) <= 1:
        return "Sorted"
    if num_sequence[0] > num_sequence[1]:
        return "Not sorted"
    return check_if_sorted_asc(num_sequence[1:])


def binary_search_recursive(sorted_seq, target_val, left_idx=0, right_idx=None):
    if right_idx is None:
        right_idx = len(sorted_seq) - 1
        
    if left_idx > right_idx:
        return "Element not found"
        
    mid_idx = (left_idx + right_idx) // 2
    
    if sorted_seq[mid_idx] == target_val:
        return f"Element found at index {mid_idx}"
    elif sorted_seq[mid_idx] > target_val:
        return binary_search_recursive(sorted_seq, target_val, left_idx, mid_idx - 1)
    else:
        return binary_search_recursive(sorted_seq, target_val, mid_idx + 1, right_idx)



if __name__ == "__main__":
    print("Task 1:"); display_ascending(5); print("\n")
    print("Task 2:"); display_descending(5); print("\n")
    print("Task 3:", sum_natural_recursive(5))
    print("Task 4:", calculate_factorial(5))
    print("Task 5:", compute_power(2, 4))
    print("Task 6:", sum_of_digits_recursive(572))
    print("Task 7:", count_digits_recursive(5729))
    print("Task 8:", reverse_integer(1234))
    print("Task 9:", get_nth_fibonacci(6))
    print("Task 10 (level):", is_text_palindrome("level"))
    print("Task 10 (hello):", is_text_palindrome("hello"))
    print("Task 11:", sum_of_sequence([3, 5, 2, 7]))
    print("Task 12:", find_max_recursive([4, 9, 1, 7, 3]))
    print("Task 13:", count_target_occurrences([1, 2, 3, 2, 2, 5], 2))
    print("Task 14:", linear_search_recursive([4, 7, 1, 9, 3], 9))
    print("Task 15 (sorted):", check_if_sorted_asc([1, 2, 4, 7, 9]))
    print("Task 15 (unsorted):", check_if_sorted_asc([1, 5, 3, 8]))
    print("Task 16:", binary_search_recursive([1, 3, 5, 7, 9, 11], 7))