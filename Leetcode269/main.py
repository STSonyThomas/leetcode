from collections import defaultdict
from typing import List
import time

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        mp={c:set() for word in words for c in word}
        for i in range(len(words)-1):
            w1=words[i]
            w2=words[i+1]
            mLen = min(len(w1),len(w2))
            if len(w1)>len(w2) and w1[:mLen]==w2[:mLen]:
                return ""
            for j in range(mLen):
                if w1[j]!=w2[j]:
                    mp[w1[j]].add(w2[j])
                    break
        visited={}# true for visited and not completed, false for visited and completed
        res=[]
        #makes use of topological sort
        def dfs(c:str):
            if c in visited:
                return visited[c]
            visited[c]=True
            for nbr in mp[c]:
                if dfs(nbr):
                    return True
            visited[c]=False
            res.append(c)
        for char in mp:
            if dfs(char):
                return ""
        res.reverse()
        return "".join(res)

# Driver code
if __name__ == "__main__":
    # Example input
    words = ["wrt", "wrf", "er", "ett", "rftt"]
    
    # Create an instance of the Solution class
    solution = Solution()
    
    # Measure execution time
    start_time = time.perf_counter()
    
    # Run the function
    result = solution.foreignDictionary(words)
    
    # Calculate execution time
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    
    # Print results
    print(f"Input: {words}")
    print(f"Output: {result}")
    print(f"Execution time: {execution_time:.6f} seconds")

