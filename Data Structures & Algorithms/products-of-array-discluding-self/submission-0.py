class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        done=-1
        ans=[]
        for i in range(len(nums)):
            done=i
            x=1
            for j in range(len(nums)):
                if j==done:
                    continue
                else:
                    x*=nums[j]
            ans.append(x)
        return ans
                
        