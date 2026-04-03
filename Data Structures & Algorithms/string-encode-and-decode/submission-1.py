class Solution:

    def encode(self, strs: List[str]) -> str:
        # count character and generate encoding
        # "Hello","World" -> 1H1e2l1o#1W1o1r1l1d
        encoded_string = ""
        for st in strs:
            encoded_string+=f"{len(st)}#{st}"
        print(f"encoded - {encoded_string}")
        return encoded_string
    
    def decode(self, st: str) -> List[str]:
        res, i = [], 0        
        while i<len(st):
            # j represent integer string length
            j=i
            while st[j]!='#':
                j+=1
            # string length
            length = int(st[i:j])            
            # get the word, j=#, so j+1 -> j+1+length
            res.append(st[j+1 : j+1+length])
            # update i to point to end of word
            i=j+1+length
        print(res)
        return res
    
