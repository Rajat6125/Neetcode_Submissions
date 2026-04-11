class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        
        # count frequency
        for i in nums:
            seen[i] = seen.get(i, 0) + 1
        
        # sort by frequency (descending)
        sorted_items = sorted(seen.items(), key=lambda x: x[1], reverse=True)
        
        # take top k elements
        result = [item[0] for item in sorted_items[:k]]
        
        return result