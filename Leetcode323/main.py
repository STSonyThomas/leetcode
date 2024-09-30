from collections import defaultdict,deque
from typing import List
from time import perf_counter

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # traveling solution
        mp=defaultdict(list)
        for [src,dest] in edges:
            mp[dest].append(src)
            mp[src].append(dest)
        walks=defaultdict(list)
        visited=[0]*n
        gc=0
        for i in range(n):
            if visited[i]:
                continue
            que = deque([i])
            while que:
                curr =que.popleft()
                visited[curr]=1
                for node in mp[curr]:
                    if not visited[node]:
                        que.append(node)
            gc+=1
        print(mp)
        print(gc)
        return gc

# Driver code
if __name__ == "__main__":
    solution = Solution()
    n = 5
    edges = [[0, 1], [1, 2], [3, 4]]
    
    start_time = perf_counter()
    result = solution.countComponents(n, edges)
    end_time = perf_counter()
    
    print(f"Number of connected components: {result}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")