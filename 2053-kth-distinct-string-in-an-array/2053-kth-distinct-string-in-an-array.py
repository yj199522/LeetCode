class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dic={}
        c=0
        for i in arr:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        for i in arr:
            if dic[i]==1:
                c+=1
                if c==k:
                    return i
        return ''
        # result = ''
        # duplicate = []
        # start = 1
        # for item in arr:
        #     if item in duplicate:
        #         continue
        #     elif arr.count(item) > 1:
        #         duplicate.append(item)
        #     elif start == k:
        #         return item
        #     else:
        #         start+=1
        # return ''
            
            
        