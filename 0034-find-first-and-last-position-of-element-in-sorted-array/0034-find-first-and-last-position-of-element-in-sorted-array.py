class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binarySearch(nums, target, is_searching_left):
            l, r = 0, len(nums) - 1
            idx = -1
            
            while l <= r:
                mid = (l + r) // 2
                
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    idx = mid
                    if is_searching_left:
                        r = mid - 1
                    else:
                        l = mid + 1
                        
            return idx

        left_bound = binarySearch(nums, target, True)
        right_bound = binarySearch(nums, target, False)
        
        return [left_bound, right_bound]