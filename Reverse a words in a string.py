class Solution(object):
    def reverseWords(self, s):
        s=s.split()
        a=s[::-1]
        return ' '.join(a)
