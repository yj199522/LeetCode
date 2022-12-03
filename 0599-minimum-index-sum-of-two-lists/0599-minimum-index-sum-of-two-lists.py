class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        result = []
        minValue = float('inf')
        mapping = {}
        if len(list2) > len(list1):
            list1, list2 = list2, list1
    
        for index in range(len(list1)):
            mapping[list1[index]] = index
    
        for index in range(len(list2)):
            if list2[index] in mapping:
                sumValue = mapping[list2[index]] + index
                if minValue >  sumValue:
                    minValue = sumValue
                    result = [list2[index]]
                elif minValue == sumValue:
                    result.append(list2[index])
        return result
                
                
        