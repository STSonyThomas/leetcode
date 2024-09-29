from typing import Dict,List
from collections import defaultdict,deque
from time import perf_counter  

class Solution1:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        start_time = perf_counter()  
        mp=defaultdict(list)
        for dest, src in prerequisites:
            mp[src].append(dest)
        visited=set()
        rec_stack = set()

        for key in range(numCourses):
            if key not in visited:
                if not self.dfs(mp,key,visited,rec_stack):
                    return False
        end_time = perf_counter()  
        print(f"Execution time: {end_time - start_time} seconds")  
                
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
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Determines if all courses can be finished given the number of courses and their prerequisites.

        Args:
            numCourses (int): The total number of courses.
            prerequisites (List[List[int]]): A list of prerequisite pairs where each pair [a, b] 
                                               indicates that course a must be completed before course b.

        Returns:
            bool: True if all courses can be finished, False otherwise.

        Time Complexity: O(V + E)
        Space Complexity: O(V + E)
        Concepts: Graphs, Topological Sort, Hashmaps, Kahn's Algorithm

        """
        if numCourses < 2:
            return True
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1
        queue = deque(i for i in range(numCourses) if in_degree[i] == 0)
        completed_courses = 0

        while queue:
            course = queue.popleft()
            completed_courses += 1
            for elem in graph[course]:
                in_degree[elem] -= 1
                if in_degree[elem] == 0:
                    queue.append(elem)
        return completed_courses == numCourses
# Driver code
if __name__ == "__main__":  
    solution1 = Solution1()
    numCourses = 2
    prerequisites = [[1, 0]]  
    start_time = perf_counter()  
    result1 = solution1.canFinish(numCourses, prerequisites)
    end_time = perf_counter()  
    print(f"Solution1 - Can finish courses: {result1}, Execution time: {end_time - start_time} seconds")  # {{ edit_8 }}

    # Timer for Solution
    solution2 = Solution()
    start_time = perf_counter() 
    result2 = solution2.canFinish(numCourses, prerequisites)
    end_time = perf_counter()  
    print(f"Solution - Can finish courses: {result2}, Execution time: {end_time - start_time} seconds")  # {{ edit_11 }}
