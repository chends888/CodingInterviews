'''
Rubric:
    | # Passing  |       |
    |   tests    | Grade |
    |--------------------|
    |   < 4      |  D    |
    |     4      |  C    |
    |     6      |  C+   |
    |     8      |  B    |
    |     10     |  B+   |
    |     12     |  A    |
    |     14     |  A+   |
'''

def pre_order_recursive(root):
    res = [root.value]
    if (root.left):
        res += pre_order_recursive(root.left)
    if (root.right):
        res += pre_order_recursive(root.right)
    return res


def pre_order_iterative(root):
    stack = []
    res = []
    stack.append(root)
    while (stack):
        node1 = stack.pop()
        res.append(node1.value)
        # Add the right child first, then the left, so we will get all 'lefts' first
        if (node1.right):
            stack.append(node1.right)
        if (node1.left):
            stack.append(node1.left)
    return res


def in_order_recursive(root):
    res = []
    if (root.left):
        res += in_order_recursive(root.left)
    res +=[root.value]
    if (root.right):
        res += in_order_recursive(root.right)
    return res

def in_order_iterative(root):
    stack = []
    res = []
    checked = []
    stack.append(root)
    while(stack):
        node1 = stack[-1]
        if (node1.right and node1.left and node1.right not in checked and node1.left not in checked):
            stack.pop()
            stack.append(node1.right)
            stack.append(node1)
            stack.append(node1.left)
        elif (node1.right and node1.right not in checked and not node1.left):
            stack.pop()
            res.append(node1.value)
            stack.append(node1.right)
            
        elif (node1.left and node1.left not in checked and not node1.right):
            stack.append(node1.left)

        # Checking if we had already passed through a node, if yes, we add it's value to 'res' and remove it from the stack
        if (node1 in checked):
            res.append(node1.value)
            stack.pop()
        else:
            checked.append(node1)
    return res

def post_order_recursive(root):
    res = []
    if (root.left):
        res += post_order_recursive(root.left)
    if (root.right):
        res += post_order_recursive(root.right)
    return res+[root.value]

def post_order_iterative(root):
    stack = []
    res = []
    checked = []
    stack.append(root)
    while(stack):
        node1 = stack[-1]
        # Only add childs to the stack if we haven't passed through them already
        if (node1.right and node1.right not in checked):
            stack.append(node1.right)
        if (node1.left and node1.left not in checked):
            stack.append(node1.left)
        if (node1 in checked):
            res.append(node1.value)
            stack.pop()
        else:
            checked.append(node1)
    return res


def breadth_first(root):
    res = []
    adjs = [root]
    while (adjs):
        for adj in adjs:
            # print(adj.value)
            res.append(adj.value)
            if (adj.left):
                adjs.append(adj.left)
            if (adj.right):
                # res.append()
                adjs.append(adj.right)
            adjs.pop(0)
            break
    return res

