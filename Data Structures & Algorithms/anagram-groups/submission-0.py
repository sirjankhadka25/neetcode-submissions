class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        seen={}
        for gram in strs:
            grams="".join(sorted(gram))
            if grams not in seen:
                seen[grams]=[]
            seen[grams].append(gram)

        
        
        return list(seen.values())





        




        