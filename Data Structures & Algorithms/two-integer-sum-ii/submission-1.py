class Two_Pointer:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            cur_sum = numbers[l] + numbers[r]

            if cur_sum > target:
                r -= 1
            elif cur_sum < target:
                l += 1
            else:
                return [l + 1, r + 1]

        return []

# Time Complexity: O(n)
# Space Complexity: O(1)


class Hash_Map:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = defaultdict(int)
        for i in range(len(numbers)):
            tmp = target - numbers[i]

            if mp[tmp]:
                return [mp[tmp], i + 1]

            mp[numbers[i]] = i + 1

        return []

# Time Complexity: O(n)
# Space Complexity: O(n)


class Binary_Search:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            l, r = i + 1, len(numbers) - 1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r - l)//2
                if numbers[mid] == tmp:
                    return [i + 1, mid + 1]
                elif numbers[mid] < tmp:
                    l = mid + 1
                else:
                    r = mid - 1
        return []

# Time Complexity: O(n log n)
# Space Complexity: O(1)

Solution = Two_Pointer