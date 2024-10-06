# Majority Element Solution

## Approach
* Uses Moore's Voting Algorithm
* Time Complexity: O(n)
* Space Complexity: O(1)
* Concepts: Arrays, Moore's Voting Algorithm

[Link to problem](https://leetcode.com/problems/majority-element/)
<u>Leetcode Problem Number #169</u>
**STATUS**: _Accepted_

## Moore's Voting Algorithm Explanation
Moore's Voting Algorithm is an efficient algorithm for finding the majority element in an array. It works on the principle that if a majority element exists (an element that appears more than n/2 times in an array of n elements), it will always remain after repeatedly removing two different elements from the array.

The algorithm works as follows:
1. Initialize two variables:
   - `res`: to store the potential majority element
   - `maxCount`: to keep track of the count
2. Iterate through the array:
   - If `maxCount` is 0, set `res` to the current element
   - If the current element is the same as `res`, increment `maxCount`
   - If the current element is different from `res`, decrement `maxCount`
3. At the end of the iteration, `res` will hold the majority element

This algorithm is highly efficient as it solves the problem in a single pass through the array and uses constant extra space.

## Implementation Details
The solution is implemented in Python. It uses the `typing` module for type hinting and the `perf_counter` function from the `time` module to measure execution time.

The `majorityElement` function in the `Solution` class implements Moore's Voting Algorithm. The driver code demonstrates how to use the solution and provides execution time measurement.
