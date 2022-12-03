class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # result = []
        # minValue = float('inf')
        # mapping = {}
        # if len(list2) > len(list1):
        #     list1, list2 = list2, list1
        # for index, word in enumerate(list1):
        #     mapping[word] = index
        # for index, word in enumerate(list2):
        #     if word not in mapping:
        #         continue
        #     sumValue = mapping[word] + index
        #     if minValue >  sumValue:
        #         minValue = sumValue
        #         result = [word]
        #     elif minValue == sumValue:
        #         result.append(word)
        hashmap = {}
        for i in range(len(list1)):   #step 1
            hashmap[list1[i]] = i
        
        res = []

        minsum = float("inf")   #step 2
        
        for j in range(len(list2)):    #step 3
            if list2[j] in hashmap:
                Sum = j + hashmap[list2[j]]    #step 3a
                
                if Sum < minsum:   #step 3b
                    minsum = Sum
                    res = []
                    res.append(list2[j])
                elif Sum == minsum:     #step 3c
                    res.append(list2[j])
        return res
        # for index1, wordforlist1 in enumerate(list1):
        #     if wordforlist1 not in list2:
        #         continue
        #     elif wordforlist1 in list2:
        #         sumIndexValue = list2.index(wordforlist1)+index1
        #         if minValue >  sumIndexValue:
        #             minValue = sumIndexValue
        #             result = [wordforlist1]
        #         elif minValue == sumIndexValue:
        #             result.append(wordforlist1)
        return result
                
                
        