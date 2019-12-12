class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        row = False
        for i in range(N-1):
            print(K)
            if (K % 2 == 0):
                row = not row
            K = K / 2
            K = math.ceil(K)
            if (K == 0):
                K = 1

        if (row):
            row = 1
        else:
            row = 0
        return row