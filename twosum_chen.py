class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            complement = target - nums[i]
            try:
                num2index = nums.index(complement)
                if (i != num2index):
                    return[i,num2index]
            except:
                pass