class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        del_count = 0
        for i, n in enumerate(nums.copy()):
            if n == val:
                del(nums[i-del_count])
                del_count += 1
        return len(nums)