class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        temp=score[:]
        temp.sort(reverse=True)
        scoredict={}
        for i in range(len(temp)):
            scoredict[temp[i]]=i+1
        ans=[]
        for i in range(len(score)):
            rank=scoredict[score[i]]
            if rank==1:
                rank="Gold Medal"
            elif rank==2:
                rank="Silver Medal"
            elif rank==3:
                rank="Bronze Medal"
            else:
                rank=str(rank)
            ans.append(rank)
        return ans
                   

        






