# Pacific Atlantic Water Flow

## 1. **Approach**

### **Solution1: Breadth-First Search (BFS)**
Solution1 utilizes the BFS algorithm to traverse the grid from the borders of both the Pacific and Atlantic oceans simultaneously. It starts by initializing queues for both oceans with their respective border cells and marks them as reachable. By exploring all possible directions (up, down, left, right) from each cell, it determines which cells can flow to both oceans.

- **Time:** *Time: 39 ms*
- **Concepts:** BFS, Graphs

### **Solution2: Depth-First Search (DFS)**
Solution2 employs the DFS algorithm to explore reachable cells from the borders of the Pacific and Atlantic oceans. It recursively traverses each possible direction from a given cell, marking cells as reachable. The intersection of cells reachable by both DFS traversals yields the final result.

- **Time:** *Time: 45 ms*
- **Concepts:** DFS, Graphs

### **Differences and Why Solution1 is Better**

1. **Traversal Strategy:**
   - **BFS vs. DFS:** Solution1's BFS approach explores neighbors level by level, which can be more efficient in terms of avoiding deep recursion stacks that DFS might encounter, especially on large grids.
   
2. **Performance:**
   - **Execution Time:** As evidenced by the execution times, Solution1 (BFS) is faster (39 ms) compared to Solution2 (DFS) which takes slightly longer (45 ms). BFS tends to perform better in scenarios where the solution is closer to the starting point.
   
3. **Space Complexity:**
   - **Queue vs. Recursion Stack:** BFS uses queues which can be more memory-efficient compared to DFS’s recursion stack, reducing the risk of stack overflow on very large inputs.

4. **Readability and Maintainability:**
   - **Iterative vs. Recursive:** Solution1's iterative BFS is generally easier to understand and maintain compared to Solution2's recursive DFS, which can become complex with multiple recursive calls.

Overall, **Solution1** is preferred due to its better execution time, efficient memory usage, and simpler iterative implementation.

**<u>Output</u>**
* Solution1 Result: [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
* Solution1 Execution Time: 0.000123 seconds
* Solution2 Result: [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
* Solution2 Execution Time: 0.000150 seconds
* Both solutions produce the same result.

[Link to problem](https://leetcode.com/problems/pacific-atlantic-water-flow/)
<u>Leetcode Problem Number #417</u>
**STATUS** : _Accepted_ 