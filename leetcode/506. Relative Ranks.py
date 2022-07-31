class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        lst = []
        rtn = ['' for i in range(len(score))]
        for i in range(len(score)):
            tpl = (i,score[i])
            lst.append(tpl)
        lst = sorted(lst,key = lambda x : x[1],reverse=True)
        for i in range(len(score)):
            ind = lst[i][0]
            if i == 0:
                rtn[ind] = "Gold Medal"
            elif i == 1:
                rtn[ind] = "Silver Medal"
            elif i ==2:
                rtn[ind] = "Bronze Medal"
            else:
                rtn[ind] = str(i+1)
        return rtn