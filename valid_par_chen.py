class Solution:
    def isValid(self, s):
        # s2 acts as a stack
        # Whenever a open-close pair is detected, they are removed from the "stack"
        s2 = ''
        for brac in s:
            s2 += brac
            if (len(s2) > 1):
                # Check if the last two chars are a pair
                if (((s2[-2] == '(') and (s2[-1] == ')')) or ((s2[-2] == '[') and (s2[-1] == ']')) or ((s2[-2] == '{') and (s2[-1] == '}'))):
                    # Remove the pair from the "stack"
                    s2 = s2[:-2]
        if(len(s2) == 0):
            return True
        return False