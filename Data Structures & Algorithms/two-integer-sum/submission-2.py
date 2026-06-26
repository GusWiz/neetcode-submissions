class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        h_num = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in h_num:
                return [h_num[complement], i]
            
            h_num[nums[i]] = i
        
        return []