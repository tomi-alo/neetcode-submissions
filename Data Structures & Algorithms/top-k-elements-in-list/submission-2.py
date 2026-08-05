class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = {}
        result = []

        for num in nums:
            if num in numbers:
                numbers[num] += 1
            else:
                numbers[num] = 1

        result = sorted(numbers, key=numbers.get, reverse=True)
        return result[:k]