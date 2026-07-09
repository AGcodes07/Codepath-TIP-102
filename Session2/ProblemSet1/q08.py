"""
Given a 0-indexed integer array nums, write a function left_right_difference that returns a 0-indexed integer array answer where:

len(answer) == len(nums)
answer[i] = left_sum[i] - right_sum[i]
Where:

left_sum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, left_sum[i] = 0
right_sum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, right_sum[i] = 0

Example Usage

nums = [10, 4, 8, 3]
left_right_difference(nums)

nums = [1]
left_right_difference(nums)
Example Output:

[-15, -1, 11, 22]
[0]
"""

def left_right_difference(nums):
    total = sum(nums)
    left = 0
    answer = []
    for x in nums:
        right = total - left - x
        answer.append(left - right)
        left += x
    return answer


nums = [10, 4, 8, 3]
print(left_right_difference(nums))

nums = [1]
print(left_right_difference(nums))