from typing import List


def calculate_products(nums: List[int]) -> List[int]:
    """
    Given a list of integers, return a new list such that each element at index i is the product of all the numbers in the original list except the one at i.

    Examples:
    >>> calculate_products([1, 2, 3, 4])
    [24, 12, 8, 6]

    >>> calculate_products([1, 0, 3, 4])
    [0, 12, 0, 0]

    >>> calculate_products([])
    []

    >>> calculate_products([5])
    [1]
    
    :param nums: List of integers
    :return: List of integers where each index i is the product of all elements except nums[i]
    :raises ValueError: If nums is not a list or if elements of nums are not integers.
    """
    # Validate input
    if not isinstance(nums, list):
        raise ValueError("Input must be a list of integers.")

    for num in nums:
        if not isinstance(num, int):
            raise ValueError("All elements in the list must be integers.")

    n = len(nums)
    # Edge cases for empty and single element lists
    if n == 0:
        return []
    if n == 1:
        return [1]

    # Count zeros in the list
    zero_count = nums.count(0)

    # If more than one zero, then all products will be zero since every entry has at least one zero.
    if zero_count > 1:
        return [0] * n
    
    # If exactly one zero, compute product of non-zero elements
    if zero_count == 1:
        total_product = 1
        for num in nums:
            if num != 0:
                total_product *= num
        # All positions except the one with zero returns 0, the position with zero gets the total_product
        result = [0] * n
        for i in range(n):
            if nums[i] == 0:
                result[i] = total_product
        return result

    # When there are no zeros, we can compute the total product and then for each element 
    total_product = 1
    for num in nums:
        total_product *= num
    
    result = [total_product // num for num in nums]
    return result


if __name__ == '__main__':
    # Basic tests
    test_cases = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([1, 0, 3, 4], [0, 12, 0, 0]),
        ([], []),
        ([5], [1]),
        ([0, 0, 3, 4], [0, 0, 0, 0])
    ]

    for test_input, expected in test_cases:
        result = calculate_products(test_input)
        print(f"Input: {test_input} => Output: {result} (Expected: {expected})")
        assert result == expected, f"Test failed for input {test_input}. Expected {expected}, got {result}."

    print("All tests passed.")
