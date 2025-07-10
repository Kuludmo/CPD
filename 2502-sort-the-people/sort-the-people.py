class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        x= list(zip(heights,names))
        x.sort(reverse=True)
        name=[]
        for i in x:
            name.append(i[1])
        return name
            

        