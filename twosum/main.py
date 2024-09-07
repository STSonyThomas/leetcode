from typing import List
import time
class Solution:
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        '''
        Hash table solution takes 27 milliseconds
        o(n)
        '''
        dixt={}
        
        for i,num in enumerate(nums):
            complement=target-num
            if complement in dixt:
                return [i,dixt[complement]]
            else:
                dixt[num]=i
        
        return [-1,-1]
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        '''
        Brute force solution takes 42 milliseconds
        o(n^2)
        '''
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return [-1,-1]


if __name__ == "__main__":
    nums=[2,7,11,15]
    target=9
    start =time.perf_counter()
    s=Solution()
    result=s.twoSum1(nums,target)
    resultTime = (time.perf_counter() - start) *1000
    print(result,"time elapsed: ",resultTime)
    start =time.perf_counter()
    result=s.twoSum2(nums,target)
    resultTime = (time.perf_counter() - start) *1000
    print(result,"time elapsed: ",resultTime)

        