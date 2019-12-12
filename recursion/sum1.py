from tree import Tree

def sum_all(A, n):
    if (n == -1):
        return 0
    else:
        A[n]+=sum_all(A, n-1)
        return A[n]

# A = [1, 2, 2,3,4,5]
# print(sum_all(A, len(A)-1))

def sum_digits(n):
    def sum_digits_r(n, sum=0):
        # print(n)
        if (n > 0):
            if (n%10 == 0):
                sum = sum_digits_r(n//10)
            else:
                sum += 1
                sum += sum_digits_r(n-1)
        # print(n, sum)
        return sum
    return sum_digits_r(n)

# print(sum_digits(333))

def sum_tree(root):
    res = root.value
    if (root.left):
        res += sum_tree(root.left)
    if (root.right):
        res += sum_tree(root.right)
    return res


# tree = Tree(list(range(3)))
# print(tree)
# print()
# print(sum_tree(tree.root))


def max_tree(root):
    res = root.value
    if (root.left):
        res2 = max_tree(root.left)
        if (res2 > res):
            res = res2
    if (root.right):
        res3 = max_tree(root.right)
        if (res3 > res):
            res = res3
    # if (root.value >):
    return res

# tree = Tree(list(range(9999)))
# print(tree)
# print()
# print(max_tree(tree.root))


def k_elem(root):
    res = [root.value]
    if (root.left):
        res += pre_order_recursive(root.left)
    return res