class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        colDeleted = 0
        for col in zip(*strs):
            if list(col) != sorted(col):
                colDeleted+=1
        return colDeleted
        # rows = len(strs)
        # cols = len(strs[0])
        # colDeleted = 0
        # for col in range(cols):
        #     for row in range(rows-1):
        #         if (strs[row][col] > strs[row+1][col]):
        #             colDeleted+=1
        #             break
        # return colDeleted
        