class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left = 0
        right = len(s)-1
        print(s)
        while(left<right):
            if(s[left] == ' ' or not s[left].isalnum()):
                left+=1
                continue
            if(s[right] == ' ' or not s[right].isalnum()):
                right-=1
                continue
            if(s[left] != s[right]):
                return False
            else:
                left+=1
                right-=1
        
        return True
        