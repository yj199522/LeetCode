class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=''
        
        strs.sort(key = len)
        
        for i in range(len(strs[0])):
            value = strs[0][i]
            
            for j in range(1,len(strs)):
                if value!= strs[j][i]:
                    
                    return res
                
            res+=value
            
        return res
        