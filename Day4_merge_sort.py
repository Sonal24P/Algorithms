class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)>1:
            #divide Array in two parts
            left =nums[:len(nums)//2]
            right =nums[len(nums)//2:]
            Solution.sortArray(self,left)
            Solution.sortArray(self,right)

            #merge arrays
            i,j,k=0,0,0
            while i<len(left) and j<len(right):
                if left[i]>right[j]:
                    nums[k]=right[j]
                    j+=1
                else:
                    nums[k]=left[i]
                    i+=1
                k+=1
            while i<len(left):
                nums[k]=left[i]
                i+=1
                k+=1
            while j<len(right):
                nums[k]=right[j]
                j+=1
                k+=1
            return nums
        else:
            return nums