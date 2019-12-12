
import math

class Solution:
    def jump(self, nums):
        def jump_r(nums, i=0, tmp_jmp=0):
            jmps = math.inf
            if (i >= len(nums - 1)):
                return tmp_jmp
            for j in range(nums[i]):
                i += 1
                print(nums[j+1], i, tmp_jmp + 1)
                tmp_jmp2 = jump_r(nums, i, tmp_jmp + 1)
                if (tmp_jmp2 < jmps):
                    jmps = tmp_jmp2
        jump_r(nums)






nums = [2, 3, 1, 1, 4]
# out = 2
sol = Solution()
sol.jump(nums)