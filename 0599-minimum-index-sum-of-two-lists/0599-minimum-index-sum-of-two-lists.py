class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        result = {}
        for index1, wordforlist1 in enumerate(list1):
            if wordforlist1 in list2:
                sumIndexValue = list2.index(wordforlist1)+index1
                if sumIndexValue not in result:
                    result[sumIndexValue] = [wordforlist1]
                else:
                    result[sumIndexValue].append(wordforlist1)
        index = sorted(list(result.keys()))
        return result[index[0]]
                
                
        