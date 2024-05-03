class Solution:
    def binarySearch(self, nums, beg, end, target):
        if beg > end:
            return -1
        mid = (beg + end) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            return self.binarySearch(nums, beg, mid - 1, target)
        else:
            return self.binarySearch(nums, mid + 1, end, target)

    def search(self, nums, target):
        beg, end = 0, len(nums) - 1
        return self.binarySearch(nums, beg, end, target)

# Example usage:
solution = Solution()
nums = [1, 3, 5, 7, 9, 11, 13]
target = 9
print(solution.search(nums, target))  # Output: 4 (index of target element)
