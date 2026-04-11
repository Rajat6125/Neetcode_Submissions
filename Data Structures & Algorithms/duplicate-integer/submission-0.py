class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map={}
        for i in nums:
            if i not in map:
                map[i]=0
            else:
                return True
        return False