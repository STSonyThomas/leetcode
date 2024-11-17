from typing import Optional
import pytest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth,right_depth)+1

def test_max_depth():
    # Test case 1: Empty tree
    assert Solution().maxDepth(None) == 0

    # Test case 2: Single node tree
    root = TreeNode(1)
    assert Solution().maxDepth(root) == 1

    # Test case 3: Tree with two nodes
    root = TreeNode(1, TreeNode(2))
    assert Solution().maxDepth(root) == 2

    # Test case 4: Tree with multiple nodes
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert Solution().maxDepth(root) == 2

    # Test case 5: Tree with multiple levels
    root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
    assert Solution().maxDepth(root) == 3

if __name__ == "__main__":
    pytest.main()