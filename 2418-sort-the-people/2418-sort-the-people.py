class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # sortedHeight = sorted(heights, reverse=True)
        # result = []
        # for height in sortedHeight:
        #     result.append(names[heights.index(height)])
        # return result
        return [name for name, _ in sorted(
            zip(names, heights),
            key=lambda x: x[1],
            reverse=True,
        )]