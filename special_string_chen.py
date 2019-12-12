class Solution:
    def is_valid(self, S):
        ones = 0
        zeros = 0
        for char in S:
            if char == '1':
                ones += 1
            else:
                zeros += 1
            if (zeros > ones):
                return False
        if (ones == zeros):
            return True
        else:
            return False
    def makeLargestSpecial(self, S: str) -> str:
        # String will always be "special binary"
        best_S = S

        # "Heights" list for detecting possible swappable strings
        heights = [0]
        for char in S:
            if(char == '1'):
                try:
                    heights.append(heights[-1] + 1)
                except:
                    heights.append(1)
            else:
                heights.append(heights[-1] - 1)
        # i is the pointer for the start of the first sub-string
        for i, _ in enumerate(heights):
            ss1_s = heights[i]
            # j is the pointer for the end of the first sub-string
            for j, ss1_e in enumerate(heights[i + 1:]):
                # Check if there's 2 of the same height, meaning a possible valid special string
                if(ss1_s == ss1_e):
                    # Special string 1 indexes
                    ss1 = [i, j + i + 1]
                    # Try to get the next special string (at the right of the first one)
                    try:
                        ss2_s = heights[j + i]
                        # k is the pointer for the end of the second sub-string
                        for k, ss2_e in enumerate(heights[j + i + 1:]):
                            if (ss2_s == ss2_e):
                                # Special string 2 indexes
                                ss2 = [ss1[1], i + j + k + 2]
                                string1 = S[ss1[0]:ss1[1]]
                                string2 = S[ss2[0]:ss2[1]]
                                # Check if both strings are special
                                if (self.is_valid(string1) and self.is_valid(string2)):
                                    # Constructing the new string
                                    new_S = S[:ss1[0]]
                                    new_S += string2
                                    new_S += string1
                                    new_S += (S[ss2[1]:])
                                    # Call a new recursion if the new string is greater than the current one, and update the best_S
                                    if (new_S > best_S):
                                        best_S = self.makeLargestSpecial(new_S)
                    except Exception as e:
                        print(e)
        return best_S