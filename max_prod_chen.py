class Solution:
    def maxProduct(self, words: List[str]) -> int:
        largest1 = ''
        largest2 = ''
        for w1 in words:
            for w2 in words:
                d1 = {}
                d2 = {}
                for c in w1:
                    try:
                        tmp = d1[c]
                    except:
                        d1[c] = None
                for c in w2:
                    try:
                        tmp = d2[c]
                    except:
                        d2[c] = None
                if (d1 == d2):
                    if (w1)




words = ['abcw','baz','foo','bar','xtfn','abcdef']

sol = Solution()

