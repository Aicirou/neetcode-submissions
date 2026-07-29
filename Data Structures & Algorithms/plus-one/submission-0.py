class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        cur_num = "".join(str(d) for d in digits)
        cur_num = int(cur_num) + 1

        return [int(d) for d in str(cur_num)]