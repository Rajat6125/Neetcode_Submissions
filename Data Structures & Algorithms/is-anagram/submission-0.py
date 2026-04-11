class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # seen1={}
        # seen2={}
        # for i in s:
        #     if i not in seen1:
        #         seen1[i]=1
        #     else:
        #         seen1[i]+=1
        # for i in t:
        #     if i not in seen2:
        #         seen2[i]=1
        #     else:
        #         seen2[i]+=1
        # return seen1==seen2
        
        if len(s) != len(t):
            return False
        
        count = {}
        
        for c in s:
            count[c] = count.get(c, 0) + 1
        
        for c in t:
            if c not in count:
                return False
            count[c] -= 1
            if count[c] == 0:
                del count[c]
        
        return len(count) == 0