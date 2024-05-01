class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for index in range(len(nums)-1):  # take each element from the list
            for limit in range(index,len(nums)): # take the subsequent element from the list
                if nums[index]>nums[limit]:  # alter the position when the current element is large
                    nums[index],nums[limit] =nums[limit],nums[index]    
        return nums
        