class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        ans=[]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and (i * j)%k==0:
                    ans.append(1)
                else:
                    continue
        ans=sum(ans)
        return ans
        

        