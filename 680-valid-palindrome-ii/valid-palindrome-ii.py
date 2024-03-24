class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        abcdcbca
        """
        def helper(flag):
            left,right = 0,len(s)-1
            once = False
            while left<=right:
                if s[left] == s[right]:
                    left+=1
                    right-=1
                    continue
                if once:
                    return False
                once = True
                if flag:
                    if s[left] == s[right-1]:
                        right-=1
                    elif s[left+1] == s[right]:
                        left+=1
                    else:
                        return False
                else:
                    if s[left+1] == s[right]:
                        left+=1
                    elif s[left] == s[right-1]:
                        right-=1
                    else:
                        return False
            return True
        return helper(True) or helper(False)