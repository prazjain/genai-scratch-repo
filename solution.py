from typing import List


def calculate_products(numbers: List[int]) -> List[int]:
    """
    Given a list of integers, return a new list such that each element at index i is
    the product of all numbers in the original list except the one at i.

    Examples:
    >>> calculate_products([1, 2, 3, 4])
    [24, 12, 8, 6]

    >>> calculate_products([1, 0, 3, 4])
    [0, 12, 0, 0]

    >>> calculate_products([])
    []

    >>> calculate_products([5])
    [1]
    
    Args:
        numbers (List[int]): List of integers.

    Returns:
        List[int]: A list where each element is the product of all numbers except the current index.

    Raises:
        TypeError: If input is not a list or if any element is not an integer.
    """
    # Validate input
    if not isinstance(numbers, list):
        raise TypeError('Input must be a list of integers.')
    
    for num in numbers:
        if not isinstance(num, int):
            raise TypeError('All elements in the input list must be integers.')

    n = len(numbers)
    # For an empty list, simply return an empty list
    if n == 0:
        return []

    # For a single element list, product of an empty set is defined as 1.
    if n == 1:
        return [1]

    # Count zeros in the list
    zero_count = numbers.count(0)

    # If there are more than one zero, every product will be zero
    if zero_count > 1:
        return [0] * n

    # If there is exactly one zero, compute product of non-zero numbers
    if zero_count == 1:
        product_non_zero = 1
        for num in numbers:
            if num != 0:
                product_non_zero *= num
        return [product_non_zero if num == 0 else 0 for num in numbers]

    # If there are no zeros, compute the total product and then the result by dividing
    total_product = 1
    for num in numbers:
        total_product *= num

    # It is safe to use integer division because there is no zero element
    return [total_product // num for num in numbers]


if __name__ == '__main__':
    # Some basic tests
    test_cases = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([1, 0, 3, 4], [0, 12, 0, 0]),
        ([], []),
        ([5], [1]),
        ([2, 3, 2], [6, 4, 6]),
    ]

    for input_list, expected in test_cases:
        result = calculate_products(input_list)
        print(f"Input: {input_list} | Output: {result} | Expected: {expected}")
        assert result == expected, f"Test failed for input: {input_list}"

    print("All tests passed!")