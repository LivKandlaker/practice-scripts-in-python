# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# Time Limit Exceeded --> think about better performance code

def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    Result = []
    for i in range(0, len(nums) - 2):
        for j in range(i + 1, len(nums) -1):
            for k in range(i + 2, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0 and i != j != k:
                    if [nums[i], nums[j], nums[k]] not in Result and [nums[i], nums[k], nums[j]] not in Result and [nums[j], nums[i], nums[k]] not in Result and \
                            [nums[j], nums[k], nums[i]] not in Result and [nums[k], nums[j], nums[i]] not in Result\
                            and [nums[k], nums[i], nums[j]] not in Result:
                        Result.append([nums[i], nums[j], nums[k]])
                        break

    return Result


nums = [-1, 0, 1, 2, -1, -4]
Result = threeSum(nums)
print(Result)
