class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for limit in range(len(nums)-1):  # take each element from the list
            for index in range(len(nums)-1): # take the sbsequent elements
                if  nums[index] > nums[index+1]: #compare the subsequent elements
                    nums[index],nums[index+1] =nums[index+1],nums[index] #swap the elements if the 2nd is loweer    
        return nums
        