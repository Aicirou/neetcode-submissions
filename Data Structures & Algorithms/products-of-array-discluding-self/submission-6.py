class Brute_Force:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        for i in range(n):
            prod = 1
            for j in range(n):
                if i == j:
                    continue
                prod *= nums[j]

            res[i] = prod

        return res

# Time Complexity: O(n ^ 2)
# Space Complexity: O(1) + O(n) for output array


class Division:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_cnt = 1, 0

        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt += 1
        
        if zero_cnt > 1: return [0] * len(nums)

        res = [0] * len(nums)

        for i, num in enumerate(nums):
            if zero_cnt: res[i] = 0 if num else prod
            else:
                res[i] = prod // num

        return res

# Time Complexity: O(n)
# Space Complexity: O(1) + O(n) for output array


class Prefix_Suffix:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n - 1] = 1

        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]

        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        
        for i in range(n):
            res[i] = pref[i] * suff[i]
        
        return res

# Time Complexity: O(n)
# Space Complexity: O(n)


class Prefix_Suffix_Optimal:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        pref = 1
        for i in range(0, len(nums)):
            res[i] = pref
            pref *= nums[i]

        postf = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postf
            postf *= nums[i]
        
        return res

# Time Complexity: O(n)
# Space Complexity: O(1) + O(n) for output array


Solution = Prefix_Suffix_Optimal