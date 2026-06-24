class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # brute force approach. Checking all elements in the List
        # for i, num1 in enumerate(nums):
        #     for j, num2 in enumerate(nums):
        #         if num1 == num2 and i != j:
        #             return True

        # return False
        
        # Possible Faster approach (using dict) with the number as the key
        h_map = {}
        for num in nums:
            if num in h_map:
                return True
            h_map[num] = 1
        return False