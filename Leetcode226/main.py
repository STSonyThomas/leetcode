from typing import Optional
import pytest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return

        # if right node then right node becomes left node and vice versa
        rightNode = root.right
        leftNode  = root.left
        root.right,root.left = root.left,root.right
        self.invertTree(rightNode)
        # print(root.val,end=" ")
        self.invertTree(leftNode)
        return root

def test_invert_tree():
    # Test case 1: Empty tree
    assert Solution().invertTree(None) is None

    # Test case 2: Single node tree
    root = TreeNode(1)
    inverted = Solution().invertTree(root)
    assert inverted.val == 1
    assert inverted.left is None
    assert inverted.right is None

    # Test case 3: Tree with two nodes
    root = TreeNode(1, TreeNode(2))
    inverted = Solution().invertTree(root)
    assert inverted.val == 1
    assert inverted.left is None
    assert inverted.right.val == 2

    # Test case 4: Tree with multiple nodes
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    inverted = Solution().invertTree(root)
    assert inverted.val == 1
    assert inverted.left.val == 3
    assert inverted.right.val == 2

if __name__ == "__main__":
    pytest.main()