"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:
    num_map = {
        "1": "หนึ่ง",
        "2": "สอง",
        "3": "สาม",
        "4": "สี่",
        "5": "ห้า",
        "6": "หก",
        "7": "เจ็ด",
        "8": "แปด",
        "9": "เก้า",
    }

    digit_map = {
        2: "สิบ",
        3: "ร้อย",
        4: "พัน",
        5: "หมื่น",
        6: "แสน",
        7: "ล้าน",
    }

    def number_to_thai(self, number: int) -> str:
        if number < 0:
            return "number can not less than 0"

        if number > 10_000_000:
            return "number can not more than 10,000,000"

        if number == 10_000_000:
            return "สิบล้าน"

        if number < 10:
            return self.num_map[str(number)]

        str_num = str(number)
        num_digit = len(str_num)

        result = ""
        for i, d in enumerate(str_num):
            digit = num_digit - i
            if digit == 2 and d == "2":
                result += "ยี่สิบ"
            elif digit == 2 and d == "1":
                result += "สิบ"
            elif digit == 1 and d == "1":
                result += "เอ็ด"
            elif d == "0":
                continue
            else:
                result += self.num_map[d]
                if digit > 1:
                    result += self.digit_map[digit]

        return result
