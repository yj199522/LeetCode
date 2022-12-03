class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        result = []
        minValue = float('inf')
        for index1, wordforlist1 in enumerate(list1):
            if wordforlist1 in list2:
                sumIndexValue = list2.index(wordforlist1)+index1
                if minValue >  sumIndexValue:
                    minValue = sumIndexValue
                    result = [wordforlist1]
                elif minValue == sumIndexValue:
                    result.append(wordforlist1)
        return result
                
                
        