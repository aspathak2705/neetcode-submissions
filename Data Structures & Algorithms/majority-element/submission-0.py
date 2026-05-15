class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        count=0
        length = len(nums)
        for i in range (0,len(nums)) :
            count = nums.count(nums[i])
            if count > length/2 :
                num = nums[i]
                break
        return num

        