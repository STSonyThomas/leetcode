from typing import Dict,List
from collections import defaultdict
from time import perf_counter  # {{ edit_1 }}

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        start_time = perf_counter()  # {{ edit_2 }}
        mp=defaultdict(list)
        for dest, src in prerequisites:
            mp[src].append(dest)
        visited=set()
        rec_stack = set()

        for key in range(numCourses):
            if key not in visited:
                if not self.dfs(mp,key,visited,rec_stack):
                    return False
        end_time = perf_counter()  # {{ edit_3 }}
        print(f"Execution time: {end_time - start_time} seconds")  # {{ edit_4 }}
                
        return True
    
    def dfs(self,mp:Dict,curr:int,v:set,rec_stack:set):
        v.add(curr)
        rec_stack.add(curr)

        for ix in mp[curr]:
            if ix not in v:
                if not self.dfs(mp,ix,v,rec_stack):
                    return False
            elif ix in rec_stack:
                return False
        rec_stack.remove(curr)
        return True

# Driver code
if __name__ == "__main__":  # {{ edit_5 }}
    solution = Solution()
    numCourses = 2
    prerequisites = [[1, 0]]  # Example test case
    result = solution.canFinish(numCourses, prerequisites)
    print(f"Can finish courses: {result}")  # {{ edit_6 }}
