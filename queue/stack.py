from singly_linked_list import LinkedList

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order.

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Stack? I think the linked list version is better because
   adding to the stack wont ever make us rewrite the stack, and stacks don't
   need to be easy to search. (idk if lists are actually easier to search)
"""
# 
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
#
#     def __len__(self):
#         return self.size
#
#     def push(self, value):
#         self.storage.append(value)
#         self.size += 1
#
#     def pop(self):
#         if self.size:
#             self.size -= 1
#             return self.storage.pop()


class Stack:
    def __init__(self):
        self.storage = LinkedList()

    def __len__(self):
        return self.storage.length

    def push(self, value):
        self.storage.add_to_head(value)

    def pop(self):
        if self.storage.length:
            return self.storage.remove_head()
