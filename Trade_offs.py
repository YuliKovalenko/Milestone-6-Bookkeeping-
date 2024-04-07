from typing import List, Tuple

# Brute-force approach
def find_sum(target: int, li: List[int]) -> Tuple[int, int]:
    n = len(li)
    for i in range(n):
        for j in range(i + 1, n):
            if li[i] + li[j] == target:
                return (li[i], li[j])


target_value = 5
numbers = [1, 2, 3, 4, 5]

print(find_sum(target_value, numbers))


# Time complexity: O(n^2) - nested loops iterate over all pairs of elements
# Space complexity: O(1) - no additional space used

# Optimized approach using a hash set

def find_sum_fast(target: int, li: List[int]) -> Tuple[int, int]:
    visited_numbers = set()
    for num in li:
        remaining_number = target - num
        if remaining_number in visited_numbers:
            return (remaining_number, num)
        visited_numbers.add(num)


target_value = 5
numbers = [1, 2, 3, 4, 5]

print(find_sum_fast(target_value, numbers))