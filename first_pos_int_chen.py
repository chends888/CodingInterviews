class Solution:
    def firstMissingPositive(self, nums):
        # Iterate over all elements of the array
        for i, num2 in enumerate(nums):
            # Skip iteration if the number is already on it's correct index
            if (num2 == i + 1):
                continue
            # For each position, try to swap until index - 1 == num
            for j, num in enumerate(nums):
                if (num != i - 1 and num > 0):
                    try:
                        tmp = nums[num - 1]
                        nums[num - 1] = num
                        nums[j] = tmp
                    except:
                        pass
        # Check if the num on an index is equal to that index + 1
        for i, num in enumerate(nums):
            if (num != i + 1):
                return i + 1
        return len(nums) + 1
