class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # map={}
        # for i in nums:
        #     if i not in map:
        #         map[i]=0
        #     else:
        #         return True
        # return False

        # Method 2
        seen=[]
        for i in nums:
            if i not in seen:
                seen.append(i)
            else:
                return True
        return False