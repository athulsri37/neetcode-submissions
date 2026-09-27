class Solution:
    def search(self, nums: List[int], target: int) -> int:
        largest = 0
        #index = -1
        for i in range(len(nums)-1):
            if(nums[i] > nums[i+1]):
                largest = i
                break
        #print(largest, nums[largest])
        #print(nums[:largest+1], nums[largest+1:])
        if target>=nums[0] and target<=nums[largest]:
            nums = nums[:largest+1]
            pad = 0
        else:
            nums = nums[largest+1:]
            pad = largest + 1
        print("pad = ",pad)
        l = 0 
        r = len(nums) - 1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                print("mid and pad = ", mid, pad)
                return mid+pad
            elif nums[mid] < target :
                l = mid+1
            else:
                r = mid-1
        return -1
        