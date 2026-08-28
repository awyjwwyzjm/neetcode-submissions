class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        iterated = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in iterated:
                return [iterated[diff], i]
            iterated[n] = i