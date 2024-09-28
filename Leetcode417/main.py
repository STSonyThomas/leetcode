from typing import List
from collections import deque
import time

class Solution1:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        m, n = len(heights), len(heights[0])
        pacific_reachable = [[False] * n for _ in range(m)]
        atlantic_reachable = [[False] * n for _ in range(m)]
        pacific_queue = deque()
        atlantic_queue = deque()
        
        # Initialize queues with border cells
        for i in range(m):
            pacific_queue.append((i, 0))
            atlantic_queue.append((i, n - 1))
            pacific_reachable[i][0] = True
            atlantic_reachable[i][n - 1] = True
        for j in range(n):
            pacific_queue.append((0, j))
            atlantic_queue.append((m - 1, j))
            pacific_reachable[0][j] = True
            atlantic_reachable[m - 1][j] = True
        
        # Perform BFS for both oceans
        self.bfs(heights, pacific_queue, pacific_reachable)
        self.bfs(heights, atlantic_queue, atlantic_reachable)
        
        # Collect cells reachable by both oceans
        result = [
            [i, j]
            for i in range(m)
            for j in range(n)
            if pacific_reachable[i][j] and atlantic_reachable[i][j]
        ]
        return result

    def bfs(self, heights, queue, reachable):
        m, n = len(heights), len(heights[0])
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # Check boundaries and if the new cell is higher or equal
                if 0 <= nx < m and 0 <= ny < n and not reachable[nx][ny] and heights[nx][ny] >= heights[x][y]:
                    reachable[nx][ny] = True
                    queue.append((nx, ny))

class Solution2:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pRes=set()
        aRes=set()
        #pacific ocean
        for x in range(len(heights)):
            self.dfs(x,0,pRes,heights)
            self.dfs(x,len(heights[0])-1,aRes,heights)
        for y in range(len(heights[0])):
            self.dfs(0,y,pRes,heights)
            self.dfs(len(heights)-1,y,aRes,heights)
        ansSet = pRes.intersection(aRes)
        ansList = [[item[0], item[1]] for item in ansSet]
        print(ansList)
        return ansList
    def dfs(self,x:int,y:int,res:List,mat:List[List[int]],prev=None):
        if (x,y) in res:
            return
        res.add((x,y))
        # try:
        #     val = mat[x][y]
        # except:
        #     print(x,y,prev,len(mat[0])-1)
        val = mat[x][y]
        top = x>0 and ((x-1,y) not in res) and (mat[x-1][y]>=val)
        right = y<(len(mat[0])-1) and ((x,y+1) not in res) and (mat[x][y+1]>=val)
        bottom = x<(len(mat)-1) and ((x+1,y) not in res) and (mat[x+1][y]>=val)
        left = y>0 and ((x,y-1)not in res) and (mat[x][y-1]>=val)
        if top:
            self.dfs(x-1,y,res,mat,(x,y))
        if right:
            self.dfs(x,y+1,res,mat,(x,y))
        if bottom:
            self.dfs(x+1,y,res,mat,(x,y))
        if left:
            self.dfs(x,y-1,res,mat,(x,y))
        
        return

def test_solutions():
    # Test case
    heights = [
        [1,2,2,3,5],
        [3,2,3,4,4],
        [2,4,5,3,1],
        [6,7,1,4,5],
        [5,1,1,2,4]
    ]
    
    # Test Solution1
    start_time = time.time()
    solution1 = Solution1()
    result1 = solution1.pacificAtlantic(heights)
    end_time = time.time()
    execution_time1 = end_time - start_time
    
    print("Solution1 Result:", result1)
    print(f"Solution1 Execution Time: {execution_time1:.6f} seconds")
    
    # Test Solution2
    start_time = time.time()
    solution2 = Solution2()
    result2 = solution2.pacificAtlantic(heights)
    end_time = time.time()
    execution_time2 = end_time - start_time
    
    print("Solution2 Result:", result2)
    print(f"Solution2 Execution Time: {execution_time2:.6f} seconds")
    
    # Compare results
    if set(map(tuple, result1)) == set(map(tuple, result2)):
        print("Both solutions produce the same result.")
    else:
        print("Solutions produce different results.")

if __name__ == "__main__":
    test_solutions()

