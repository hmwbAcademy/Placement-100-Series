class Solution:
    """Method-1: Using Sorting Approach """
    def containsDuplicate(self, nums: List[int]) -> bool:
        # sort the array first
        nums.sort()

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False

    """ Method-2: Hashtable """
    def containsDuplicate(self, nums: List[int]) -> bool:
        map = set()

        for each in nums:
            if each in map:
                return True

            map.add(each)

        return False