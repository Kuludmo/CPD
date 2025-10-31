class Solution(object):
    def getSneakyNumbers(self, nums):
        sneakys=[]
        for i in nums:
           if nums.count(i)>1 and i  not in sneakys:
                sneakys.append(i)
        return sneakys


        """
        :type nums: List[int]
        :rtype: List[int]
        """
        