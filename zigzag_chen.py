
def convert(s, numRows):
    if (numRows != 1):
        jmp = (numRows * 2) - 2
    else:
        jmp = 1
    complement = 0
    transformed = ''

    for i in range(numRows):
        if (i == 0 or i == numRows-1):
            j = jmp
            k = jmp
        else:
            j = jmp - (2 * i)
            k = jmp - j
        l = i
        flag = True
        while (l < len(s)):
            transformed += s[l]
            if (flag):
                l += j
                flag = False
            else:
                l += k
                flag = True

    return transformed

s = 'PAYPALISHIRING'
numRows = 4

print(convert(s, numRows))