class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num1 in enumerate(nums):
            complement = target - num1
            for j, num2 in enumerate(nums):
                if num2 == complement and i != j: 
                    if i < j:
                        return [i, j]
                    else:
                        return [j,i]

        return []