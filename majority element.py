class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l={}
        for i in nums:
            if i in l:
                l[i]+=1
            else:
                l[i]=1
        k=max(l,key=l.get)
        return k
