class Solution:
    
    def solve(self,digits,index,digit_map,output,ans):
        # Base Case
        if index >= len(digits):
            ans.append(output[:])
            return

        # Processing
        digit_ = int(digits[index])
        value_ = digit_map[digit_]
        for i in range(len(value_)):
            output.append(value_[i])
            self.solve(digits,index+1,digit_map,output,ans)
            # Backtracking
            output.pop()
    
    def letterCombinations(self, digits: str):
        digit_map = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        ans = []
        output = []
        index = 0
        self.solve(digits,index,digit_map,output,ans)
        ans1 = []
        for i in ans:
            p = ''.join(i)
            ans1.append(p)
        return ans1

t = Solution()
digits = "2354"
print(t.letterCombinations(digits))
