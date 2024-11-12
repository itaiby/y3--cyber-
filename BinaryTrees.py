from binarytree import Node

def count_occurrences(root, target):
    if root is None:
        return 0
    count = 1 if root.value == target else 0
    count += count_occurrences(root.left, target)
    count += count_occurrences(root.right, target)
    return count

def is_plaindrome(root1, root2=None):
    if root2 == None:
        root2 = root1
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    return root1.value == root2.value and is_plaindrome(root1.left, root2.right) and is_plaindrome(root1.right, root2.left)

def serialize(root):
    if root is None:
        val = "#"
    else:
        val = str(root.value)
    return val + "," + serialize(root.left) + "," + serialize(root.right)

def deserialize(list):
    if list[0] == "#":
        list.pop(0)
        return None
    root = Node(list.pop(0))
    root.left = deserialize(list)
    root.right = deserialize(list)
    return root

def save(filename, root):
    with open(filename, "w") as file:
        file.write(serialize(root))

def restore(filename):
    with open(filename, "r") as file:
        return deserialize(file.read().split(","))[0]



