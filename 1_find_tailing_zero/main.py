"""
เขียบนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""


class Solution:

    def factorial(self, number: int) -> int:
        return number * self.factorial(number - 1) if number > 1 else 1

    def find_tailing_zeroes(self, number: int) -> int | str:
        if number < 0:
            return "number can not be negative"

        fac = self.factorial(number)

        result = 0
        n = 10
        while fac % n == 0:
            result += 1
            n *= 10
        return result
