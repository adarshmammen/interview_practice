class Solution(object):
    def reverse(self, x):
        s = str(x)[::-1]
        if s[-1] == '-':
            s = '-' + s[:-1]
        s = int(s)
        if s < -2147483647 or s > 2147483647:
            return 0
        else:
            return s
            
