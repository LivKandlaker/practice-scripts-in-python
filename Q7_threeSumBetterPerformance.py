# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# Time Limit Exceeded --> N^2

def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums = sorted(nums)
    Result = []
    if nums[0] > 0 or nums[len(nums)-1] < 0:
        return Result
    for i in range(0, (len(nums) - 1)):
        num1 = len(nums) - 1
        num2 = i + 1
        while num2 != i and num1 != num2 and num1 != i and num1 > 0 and 0 < num2 < len(nums):
            if (nums[i] + nums[num1] + nums[num2]) == 0 :
                if [nums[i], nums[num1], nums[num2]] not in Result \
                       and [nums[num1], nums[i], nums[num2]] not in Result \
                        and [nums[num1], nums[num2], nums[i]] not in Result \
                        and [nums[num2], nums[num1], nums[i]] not in Result \
                        and [nums[i], nums[num2], nums[num1]] not in Result \
                        and [nums[num2], nums[i], nums[num1]] not in Result:
                    Result.append([nums[i], nums[num1], nums[num2]])
                    num1 -= 1
                    num2 += 1
                else:
                    num1 -= 1
                    num2 += 1
            elif nums[i] + nums[num1] + nums[num2] < 0:
                num2 += int(len(nums)/3)
            else:
                num1 -= int(len(nums)/3)
    return Result


nums = [3,0,-2,-1,1,2]
Result = threeSum(nums)
print(Result)
