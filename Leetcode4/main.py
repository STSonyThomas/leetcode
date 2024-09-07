from typing import List

class Solution:
    '''
    Not the best solution 
    The best solution makes use of binary search
    Have to learn that.
    '''
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # ptr1=0
        # ptr2=0
        # lenArr1=len(nums1)
        # lenArr2=len(nums2)
        # lenMerged=lenArr1+lenArr2
        lenMerged =len(nums1) +len(nums2)
        mergedArray=[]
        # while not(ptr1==lenArr1 and ptr2 ==lenArr2):
        #     num1=nums1[ptr1] if ptr1!=lenArr1 else None
        #     num2=nums2[ptr2] if ptr2!=lenArr2 else None
        #     if num1!=None and num2!=None:
        #         # print("entered num1 num2")
        #         if num1<num2:
        #             mergedArray.append(num1)
        #             ptr1+=1
        #         elif num1==num2:
        #             mergedArray.append(num1)
        #             mergedArray.append(num1)
        #             print(ptr1,ptr2,mergedArray)
        #             ptr1+=1
        #             ptr2+=1
        #         else:
        #             mergedArray.append(num2)
        #             ptr2+=1
        #     elif num1!=None:
        #         # print("entered num1 ")
        #         mergedArray+=nums1[ptr1:]
        #         break
        #     else:
        #         # print("entered num2")
        #         mergedArray+=nums2[ptr2:]
        #         break
        mergedArray=nums1 +nums2
        mergedArray.sort()
        if lenMerged%2 !=0:
            return float(mergedArray[lenMerged//2 ])
        else:
            # print(lenMerged//2,lenMerged//2 -1,mergedArray,lenArr1,lenArr2)
            val = mergedArray[lenMerged//2] + mergedArray[lenMerged//2 -1]
            return float(val/2)
        #     print(lenMerged,lenMerged/2)
        # print(mergedArray)
        # return 4.2
