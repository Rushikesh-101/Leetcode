"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        def post(node,result):
            if node is None :
                return 
            if node.children :
                for childNode in node.children:
                    post(childNode,result)
            
            result.append(node.val)

        result = []
        post(root,result)
        return result