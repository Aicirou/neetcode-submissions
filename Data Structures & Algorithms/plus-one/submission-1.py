class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_digits = "".join(str(d) for d in digits) # "1234"
        plus = int(str_digits) + 1

        return [int(ch) for ch in str(plus)]