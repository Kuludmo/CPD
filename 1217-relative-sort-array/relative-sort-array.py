class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
       # arr1=sorted(arr1)
        #return arr1
        ans=[]
        for i in arr2:
            while i in arr1:
                ans.append(i)
                arr1.remove(i)
        #return ans
        #for i in arr1:
           # if i not in arr2:
               # ans.append(i)
        #print(arr1)
        ans+=sorted(arr1)
        return ans
        


        #print (relativeSortArray)
        
        
        