class Solution(object):
    def hIndex(self, citations):
        citations.sort(reverse=False)
        max_citation=0
        print(citations)
        for i in range(len(citations)):
            # if citations[i]<=len(citations)-i:
            #     max_citation=max(citations[i],max_citation)
            if citations[i] >= len(citations) - i:
                max_citation = max(max_citation, len(citations) - i)
        if len(citations) == 1:
            return 0 if citations[0] == 0 else 1
        return max_citation