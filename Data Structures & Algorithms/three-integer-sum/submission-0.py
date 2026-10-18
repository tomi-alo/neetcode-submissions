class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[left] + nums[right] + num

                if total == 0:
                    result.append([nums[left], num, nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1
        return result
