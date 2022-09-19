from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        N = len(nums1)+len(nums2) #Gets Sum of individual List Sizes
        
        mode = N%2 # 0 -> Even TotalSize | Else -> Odd Total Size , Appopriate mid value.
        mid = N//2
    
        if(mode!=0):
            mid += 1

        temp_list = [] # Creating a list as no space complexity constraint, Append and Access is O(1)
        i=0
        j=0  
        while(len(temp_list)< mid + 1): # While till half of Combined List
            if ((i<len(nums1) and j<len(nums2))):
                if(nums1[i]<nums2[j]):
                    temp_list.append(nums1[i])
                    i+=1
                else:
                    temp_list.append(nums2[j])
                    j+=1
            elif(i<len(nums1)): # When 'nums2' has been iterated
                temp_list.append(nums1[i])
                i+=1
            else: # When 'nums1' has been iterated
                temp_list.append(nums2[j])
                j+=1
        
        if(mode==0): # Even TotalSize Case
            return ((temp_list[mid-1]+temp_list[mid]) / 2.0)
        else: # Odd TotalSize Case
            return temp_list[mid-1]
