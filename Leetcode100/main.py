from typing import Optional
import pytest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val!=q.val:
            return False
        return self.isSameTree(p.right,q.right) and self.isSameTree(p.left,q.left)

def test_is_same_tree():
    # Test case 1: Both trees are empty
    assert Solution().isSameTree(None, None) == True

    # Test case 2: One tree is empty, the other is not
    assert Solution().isSameTree(TreeNode(1), None) == False
    assert Solution().isSameTree(None, TreeNode(1)) == False

    # Test case 3: Both trees have one node with the same value
    assert Solution().isSameTree(TreeNode(1), TreeNode(1)) == True

    # Test case 4: Both trees have one node with different values
    assert Solution().isSameTree(TreeNode(1), TreeNode(2)) == False

    # Test case 5: Trees with multiple nodes, same structure and values
    tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
    tree2 = TreeNode(1, TreeNode(2), TreeNode(3))
    assert Solution().isSameTree(tree1, tree2) == True

    # Test case 6: Trees with multiple nodes, different structure
    tree1 = TreeNode(1, TreeNode(2))
    tree2 = TreeNode(1, None, TreeNode(2))
    assert Solution().isSameTree(tree1, tree2) == False

if __name__ == "__main__":
    pytest.main()

