class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadanes Algorithim
        global_max = nums[0]
        current_max = nums[0]

        for i in range(1, len(nums)):
            # want to move through and find possible maxes
            # if previous sum is less then current number than add number to sum
            # if current number is more than previous sum than start sum count on current number
            current_max = max(current_max + nums[i], nums[i])

            # want to store the max at each stage 
            global_max = max(current_max, global_max)
            

        return global_max
    

        
    
        