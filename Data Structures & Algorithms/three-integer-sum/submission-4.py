class Two_Pointer:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() #so we can do two pointer

        for i, a in enumerate(nums):
            if a > 0:
                break #all positives afterward
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue #skip duplicates

            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = a + nums[l] + nums[r]

                if three_sum == 0:
                    #append found ones
                    res.append([a, nums[l], nums[r]])
                    #process next
                    l += 1
                    r -= 1

                    #skip duplicates in inner while loop
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                
                elif three_sum < 0:
                    l += 1
                else:
                    r -= 1
        return res

# Time Complexity: O(n ^ 2)
# Space Complexity: O(1), excludes sorting and output list


Solution = Two_Pointer