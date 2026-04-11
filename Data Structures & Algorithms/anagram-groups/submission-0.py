class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keep = {}
        
        for i in strs:
            key = "".join(sorted(i))  # convert to string
            
            if key not in keep:
                keep[key] = [i]
            else:
                keep[key].append(i)
        
        return list(keep.values())