# Aim: To implement Jump Search

# Time Complexity:
# - Best Case: O(1) when the target is found in the first block.
# - Average and Worst Case: O(√n) where n is the number of elements in the array.

# :param arr: Sorted list of elements to search
# :param target: Element to search for
# :return: Index of target if found, else -1

import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))  # Optimal jump size
    prev = 0  # Previous block's start index

    # Jump through the array in steps
    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))  # Move to the next block
        if prev >= n:  # If we've exceeded the array length
            return -1

    # Perform linear search within the identified block
    while prev < n and arr[prev] < target:
        prev += 1

    # Check if the target is found
    if prev < n and arr[prev] == target:
        return prev  # Return the index if found

    return -1  # Target not found

# Example usage
if __name__ == "__main__":
    
    user_input = input("Enter sorted numbers separated by spaces: ")
    my_list = list(map(int, user_input.split()))  # Convert input to a list of integers

    target_value = int(input("Enter the target value to search for: "))  

    result = jump_search(my_list, target_value)

    # Sample working:
    # 1. Array: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
    # 2. Jump size (step): √11 ≈ 3
    # 3. First jump to index 3 (value 7) -> not found (target > 7)
    # 4. Next jump to index 6 (value 13) -> not found (target > 13)
    # 5. Next jump to index 9 (value 19) -> not found (target < 19)
    # 6. Linear search in range [6, 9]: find target 15 at index 7

    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found")



