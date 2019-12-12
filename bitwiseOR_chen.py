class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        res = []
        res2 = {}
        for elem in A:
            test = elem
            for res_elem in reversed(res):
                # Accumulate the "or" through the reversed list
                test = test | res_elem
                res2[test] = None
            res.append(elem)
        res3 = {}
        # Gather all the unique results
        for i in res:
            res3[i] = None
        for i in res2.keys():
            res3[i] = None
        return len(res3)