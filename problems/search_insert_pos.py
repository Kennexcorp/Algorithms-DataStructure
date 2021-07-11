class Solution:
    def searchInsert(self, nums, target: int):

        self.low = 0
        self.high = len(nums)-1

        while self.low <= self.high:
            
            mid = (self.low + self.high)//2
            guess = nums[mid]

            if guess == target:
                return mid

            if guess > target:
                self.high = mid - 1
            else:
                self.low = mid + 1
            

            print(self.low, self.high, guess, mid)
        
        if target > guess:
            return mid+1 
        else:
            return mid


test = Solution()
ans = test.searchInsert([1,3,5,6,7,8], 4)
print(ans)