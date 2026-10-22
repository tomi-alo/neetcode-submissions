class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            midd = (left + right) // 2

            if nums[midd] == target:
                return midd

            elif nums[midd] >= nums[left]:
                # left half is sorted
                if nums[left] <= target < nums[midd]:
                    right = midd - 1
                else:
                    # right half is sorted
                    left = midd + 1

            else:
                # right half is sorted
                if nums[midd] < target <= nums[right]:
                    left = midd + 1
                else:
                    right = midd - 1
        return -1
