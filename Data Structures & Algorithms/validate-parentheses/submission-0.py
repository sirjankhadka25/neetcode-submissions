
class Solution:
    def isValid(self, s: str) -> bool:
        dict1={'(': ')', '{':'}', '[' : ']'}
        stack=[]
        for i in s:
            if i in dict1.keys():
                stack.append(i)
            elif i in dict1.values():
                if not stack or i!=dict1[stack.pop()]:
                    return False
        return not stack
