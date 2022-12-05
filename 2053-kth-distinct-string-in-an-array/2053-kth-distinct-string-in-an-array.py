class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = collections.Counter(arr)
        for i in arr:
            if c[i] == 1:
                k-=1
                if k== 0:
                    return i
        return ""
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
            
            
        