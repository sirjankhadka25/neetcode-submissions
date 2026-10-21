class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set(nums)
        n=len(nums)
        if n>len(seen):
            return True
        else:
            return False

        