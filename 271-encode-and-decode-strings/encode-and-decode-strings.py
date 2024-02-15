class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        for s in strs:
            for c in s:
                if c == ":":
                    res += "::"
                elif c == "|":
                    res += ":|"
                else:
                    res += c
            res += "|"
        print(res)
        return res
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        res = []
        i = 0
        st = ""
        while i < len(s):
            if i != len(s) - 1:
                d = s[i] + s[i+1]
            else:
                d = s[i]
            if d == "::":
                i+=2
                st+=":"
            elif d == ":|":
                i+=2
                st+="|"
            elif s[i] == "|":
                res.append(st)
                st = ""
                i+=1
            else:
                st+=s[i]
                i+=1
                
        return res
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))