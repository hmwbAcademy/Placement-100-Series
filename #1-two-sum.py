class Solution:
  """ Method-1: Bruteforce Approach 
  def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
  """

    # Method-2: using hashmap
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            curr = nums[i]
            x = target - curr

            if hashmap.get(x, -1) == -1:
                hashmap[curr] = i

            else:
                return [i, hashmap[x]]
