class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
         nums.sort()     
         #print(nums)       
          #  for j in ans:
           #     result=min(i) + min(j)
         return sum(nums[::2])
        