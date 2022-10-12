# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
# target. You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order. Example 1: Input: nums = [2,7,11,15], target = 9 Output: [0,1] Explanation:
# Because nums[0] + nums[1] == 9, we return [0, 1].

# leetCode:
# Runtime: 2640 ms, faster than 39.10% of Python online submissions for Two Sum.
# Memory Usage: 14.3 MB, less than 45.68% of Python online submissions for Two Sum.

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    Result = [0, 0]
    for i in range(0, len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                Result = [i, j]

    return Result


nums = [4, 2, 3]
target = 7
result = twoSum(nums, target)

print(result)
