from collections import defaultdict,deque
from typing import List
import time

# check if disjoint first then if not disjoint then check for cycle
# follows kahns algorithm
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
        mp=defaultdict(list)
        comp=0
        print(mp)
        indegree=[0]*n
        for [src, dest] in edges:
            mp[dest].append(src)
            indegree[dest]+=1
            indegree[src]+=1
            mp[src].append(dest)
        que = deque(i for i in range(n) if indegree[i]==1)
        print(mp)
        print(indegree)
        print(que)
        while que:
            curr = que.popleft()
            comp+=1
            for nbr in mp[curr]:
                indegree[nbr]-=1
                if indegree[nbr]==1:
                    que.append(nbr)
        print(indegree)
        if sum(indegree)==0: 
            return True
        return False
        # return True
        # return True

def driver():
    # Example inputs
    examples = [
        (5, [[0, 1], [0, 2], [0, 3], [1, 4]]),  # Valid tree
        (5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]),  # Not a valid tree (contains a cycle)
    ]

    solution = Solution()

    for i, (n, edges) in enumerate(examples, 1):
        print(f"\nExample {i}:")
        print(f"Input: n = {n}, edges = {edges}")

        start_time = time.perf_counter()
        result = solution.validTree(n, edges)
        end_time = time.perf_counter()

        print(f"Output: {result}")
        print(f"Execution time: {(end_time - start_time) * 1000:.4f} ms")

if __name__ == "__main__":
    driver()