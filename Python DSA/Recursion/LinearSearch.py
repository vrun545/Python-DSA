class Solution:
    def linearSearch(self, nums, i, target, size):
        if i >= size:
            return -1
        if nums[i] == target:
            return i
        else:
            # Return the result of the recursive call
            return self.linearSearch(nums, i+1, target, size)
    
    def search(self, nums, target):
        size, i, ans = len(nums), 0, -1
        return self.linearSearch(nums, i, target, size)

# Example usage:
solution = Solution()
result = solution.search([1, 2, 3, 4, 5], 3)
print(result)  # Output: 2
