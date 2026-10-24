class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen={}
        for num in nums:
            seen[num]=seen.get(num,0)+1
        rank=sorted(seen,key=seen.get,reverse=True)
        return rank[:k]

        

        