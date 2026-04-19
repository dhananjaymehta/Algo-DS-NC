class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = j = 0
        len1, len2 = len(nums1), len(nums2)
        median1 = median2 = 0 
        """
        The "Two-Step" Memory Pattern
        Since the median of an even set of numbers is the average of the two middle elements, we need a way to remember the "previous" element we saw.
        median1: Represents the current smallest element found in the merge simulation.
        median2: Represents the previous smallest element found (the one right before median1).
        """       
        for count in range((len1+len2)//2+1):
            median2 = median1
            # if i and j both have element to traverse
            if i<len1 and j<len2:
                if nums1[i]<nums2[j]:
                    median1=nums1[i]
                    i+=1
                else:
                    median1=nums2[j]
                    j+=1                
            # if i still has elements
            elif i<len1:
                median1=nums1[i]
                i+=1
            # if j still has elements
            else:
                median1=nums2[j]
                j+=1
            print(median1, median2)
        if (len1+len2)%2 == 0:
            return (median1+median2)/2.0
        else:
            return float(median1)
        