
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        return self.traverseGraph(node)
        
    def traverseGraph(self, node):
        queue = [node]
        iNode = Node(node.val, [])
        track = {node.val: iNode}
        
        while queue:
            curr = queue.pop(0)
            curr_clone = track[curr.val]
            
            for neighbor in curr.neighbors:
                
                if neighbor.val not in track:
                    # Clone the neighbor
                    track[neighbor.val] = Node(neighbor.val, [])
                    queue.append(neighbor)
                curr_clone.neighbors.append(track[neighbor.val])
                    
        return iNode