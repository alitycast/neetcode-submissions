class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]

        sorted_strs = {}
        for string in strs:
            sorted_str = "".join(sorted(string))
            if sorted_strs.get(sorted_str):
                sorted_strs[sorted_str].append(string)
            else:
                sorted_strs[sorted_str] = [string]
        
        return list(sorted_strs.values())