"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BST class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BST class.
"""
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    # def insert(self, value):
    #     current = self
    #     placed = False
    #     while not placed:
    #         if value <= current.value:
    #             if current.left is None:
    #                 current.left = BST(value)
    #                 placed = True
    #             else:
    #                 current = current.left
    #         elif value > current.value:
    #             if current.right is None:
    #                 current.right = BST(value)
    #                 placed = True
    #             else:
    #                 current = current.right

    # recursive insert
    def insert(self, value):
        if value <= self.value:
            if self.left is None:
                self.left = BST(value);
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value);
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    # recursive contains
    def contains(self, target):
        if self.value == target:
            return True
        elif target <= self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # STRETCH:
    def delete(self, value):
        pass


    # Return the maximum value found in the tree
    def get_max(self):
        max = self
        while max.right is not None:
            max = max.right
        return max.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass



"""
This code is necessary for testing the `print` methods
"""
# bst = BinarySearchTree(1)
bst = BST(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
# bst.in_order_dft()
print("post order")
bst.post_order_dft()
