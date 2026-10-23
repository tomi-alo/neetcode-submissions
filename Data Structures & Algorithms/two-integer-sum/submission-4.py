class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_seen = {} # number : index

        for i, num in enumerate(nums):
            complement = target - num

            if complement in nums_seen:
                return [nums_seen[complement], i]

            nums_seen[num] = i

        return