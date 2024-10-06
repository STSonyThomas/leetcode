from typing import List
from time import perf_counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Moore's voting algorithm
        maxCount = 0
        res = None
        for num in nums:
            if maxCount == 0:
                res = num
            maxCount += 1 if res == num else -1
        return res

# Driver code
if __name__ == "__main__":
    # Example input
    nums = [2, 2, 1, 1, 1, 2, 2]
    
    solution = Solution()
    
    # Measure execution time
    start_time = perf_counter()
    result = solution.majorityElement(nums)
    end_time = perf_counter()
    
    # Print results
    print(f"Input: {nums}")
    print(f"Majority Element: {result}")
    print(f"Execution time: {(end_time - start_time) * 1000:.6f} ms")