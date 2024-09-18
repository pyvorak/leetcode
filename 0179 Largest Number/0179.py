class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(x) for x in nums]
        
        def cmp(a, b):
            return 1 if a+b <= b+a else -1

        nums.sort(key = cmp_to_key(cmp))
        ans = "".join(nums)
        return "0" if ans[0] == '0' else ans
