class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numerosvisto={}
    
        for i,num in enumerate (nums):
            diferencia=target-num

            if diferencia in numerosvisto:
                return numerosvisto[diferencia],i

            numerosvisto[num]=i
        return []
               