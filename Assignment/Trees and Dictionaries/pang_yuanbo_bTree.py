#Yuanbo Pang
# Function to construct a tree with a label and branches
def tree(label, branches=[]):
    return [label] + list(branches)



def label(tree):
    return tree[0]



def branches(tree):
    return tree[1:]



def is_leaf(tree):
    return not branches(tree)



def count_leaves(t):
    if is_leaf(t):
        return 1
    else:
        return sum(count_leaves(b) for b in branches(t))


# Function to print the tree structure
def print_tree(t, indent=0):
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)



my_tree = tree(4, [
    tree(2, [tree(1), tree(3)]),
    tree(5, [tree(6)])  # Swapped positions of 5 and 6
])


print("Nested tree structure:")
print_tree(my_tree)

# Print the root label of the tree
print(f"\nRoot label: {label(my_tree)}")

# Print the branches of the tree
print(f"Branches: {[label(b) for b in branches(my_tree)]}")

# Print the number of leaves in the tree
print(f"Number of leaves: {count_leaves(my_tree)}")
