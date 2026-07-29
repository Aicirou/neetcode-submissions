# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         str_digits = "".join(str(d) for d in digits) # "1234"
#         plus = int(str_digits) + 1

#         return [int(ch) for ch in str(plus)]

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits) - 1, -1, -1):

            if digits[i] + 1 != 10:
                digits[i] += 1
                return digits
            
            digits[i] = 0

            if i == 0:
                return [1] + digits