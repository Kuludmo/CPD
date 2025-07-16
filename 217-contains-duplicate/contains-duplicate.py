class Solution:
    def containsDuplicate(self, nums: List[int])-> bool:
        ans=set(nums)
        if len(nums)==len(ans):
            return False
        else:
            return True
        