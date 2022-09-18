class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        startrow, endrow, topcol, endcol = 0, n, 0, n
        count = 1
        result = [[0] * n for i in range(n)]
        while startrow< endrow and topcol< endcol:
            for i in range(startrow, endrow):
                result[topcol][i] = count
                count+=1
            topcol+=1
            for i in range(topcol, endcol):
                result[i][endrow-1] = count
                count+=1
            endrow-=1
            if startrow < endrow:
                for i in range(endrow-1, startrow - 1, -1):
                    result[endcol-1][i] = count
                    count+=1
                endcol-=1
            if topcol < endcol:
                for i in range(endcol -1, topcol -1, -1):
                    result[i][startrow] = count
                    count+=1
                startrow+=1
        return result