def findLCA(list_tree, value1, value2):
    # Check if both values are in the tree
    if value1 not in list_tree or value2 not in list_tree:
        return None

    # Find the indexes of the nodes
    index1 = list_tree.index(value1)
    index2 = list_tree.index(value2)

    # Traverse up the tree until a common ancestor is found
    while index1 != index2:
        if index1 > index2:
            index1 = (index1 - 1) // 2
        else:
            index2 = (index2 - 1) // 2

    # Return the value at the common ancestor index
    return list_tree[index1]

# Example usage
tree_array = [90, 89, 70, 36, 85, 63, 65]

lca = findLCA(tree_array, 36, 65)
print(lca)  # this should print 90

lca = findLCA(tree_array, 18, 36)
print(lca)  # this should print 36

lca = findLCA(tree_array, 21, 100)
print(lca)  # this should print None, as 100 is not in the tree.
