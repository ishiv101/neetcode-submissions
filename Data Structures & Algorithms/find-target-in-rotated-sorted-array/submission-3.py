class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if target is smaller than last number want to search the true section
        # if target is larger than last number want to search the false section 
        search = target <= nums[-1]
        #find first true to find border
        left = 0
        right = len(nums) - 1
        first_true_index = -1
        while left <= right:
            mid = (left + right) // 2
            if (nums[mid] <= nums[-1]) == True:
                right = mid - 1
                first_true_index = mid
            else:
                left = mid + 1
        # now binary search on True section or False section
        # False section binary search
        if search == False:
            left = 0
            right = first_true_index - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        # True section binary search
        else:
            left = first_true_index
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1





        