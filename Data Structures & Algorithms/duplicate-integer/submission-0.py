class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result=[]
        for ch in nums:
            if ch in result:
                return True
            result.append(ch)
        return False