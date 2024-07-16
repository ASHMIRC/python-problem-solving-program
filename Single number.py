class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        u=[i for i in nums if nums.count(i)==1]
        result = ''.join(map(str,u))
        return int(result)
        
