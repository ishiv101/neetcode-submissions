class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        check = nums[right]
        answer = 0
        while left <= right:
            mid = (left + right) // 2
            if (nums[mid] <= check) == True:
                right = mid - 1
                answer = mid
            else:
                left = mid + 1

        return nums[answer]
        


        