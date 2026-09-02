class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lennums = len(nums)

        for i in range(lennums - 1):
            if nums[i] == val:
                j = i + 1

                while j < lennums and nums[j] == val:
                    j += 1

                if j == lennums:
                    return i

                nums[i], nums[j] = nums[j], nums[i]

        if lennums > 0 and nums[-1] == val:
            return lennums - 1

        return lennums