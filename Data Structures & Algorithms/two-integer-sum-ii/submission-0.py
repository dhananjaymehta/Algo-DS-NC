class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        s , e = 0, n-1

        while s<e:
            if numbers[s]+numbers[e]==target:            
                return [s+1 ,e+1]
            if numbers[s]+numbers[e]>target:            
                e-=1
            else:
                s+=1            
        return [s,e]