class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string=""
        for string in strs:
            encoded_string=encoded_string+str(len(string))+"#"+string
        return encoded_string


    def decode(self, s: str) -> List[str]:
        i=0
        words=[]
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            length=int(s[i:j])
            word=s[j+1:length+j+1]

            words.append(word)
            i=length+j+1
        return words




