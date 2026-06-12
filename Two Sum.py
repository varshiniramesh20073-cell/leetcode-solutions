class Solution(object):
    def twoSum(self, nums, target):
        ak=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    ak.append(i)
                    ak.append(j)
                    return ak
