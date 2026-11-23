class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupes = {}
        for num in nums:
            if dupes.get(num):
                dupes[num] += 1
                return True
            dupes[num] = 1
        
        for num, amount in dupes.items():
            if amount > 1:
                return True
        
        return False
        

        