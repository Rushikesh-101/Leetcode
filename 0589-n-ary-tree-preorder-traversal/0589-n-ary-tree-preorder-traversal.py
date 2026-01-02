"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        result = []

        if not root:
            return result
        
        def pre(node,result):
            
            result.append(node.val)
            
            if node.children:
                for child in node.children:
                    pre(child,result)

        pre(root,result)
        return result