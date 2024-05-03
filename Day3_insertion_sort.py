class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for limit in range(len(nums)):  # take each element from the list
            for index in range(0,limit): # compare current value with all the previous elements
                if  nums[index] > nums[limit]: 
                    nums[limit],nums[index] =nums[index],nums[limit] #swap the elements if the elemnt is larger    
        return nums
        