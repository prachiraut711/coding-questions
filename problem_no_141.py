# You are given a string number representing a positive integer and a character digit.
# Return the resulting string after removing exactly one occurrence of digit from number such that the value of the resulting string in decimal form is maximized. The test cases are generated such that digit occurs at least once in number.
# Example 1:  Input: number = "123", digit = "3"  Output: "12"
# Explanation: There is only one '3' in "123". After removing '3', the result is "12".
# Example 2:  Input: number = "1231", digit = "1" Output: "231"
# Explanation: We can remove the first '1' to get "231" or remove the second '1' to get "123".
# Since 231 > 123, we return "231".
# Example 3: Input: number = "551", digit = "5" Output: "51"
# Explanation: We can remove either the first or second '5' from "551".
# Both result in the string "51".

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max_num = 0
        demo_list = list(number)
        temp = ""
        for i in range(len(demo_list)):
            if demo_list[i] == digit:
                temp = demo_list[i]
                demo_list[i] = ""
                int_num = int("".join(demo_list))
                print(int_num)

                if int_num > max_num:
                    max_num = int_num
                demo_list[i] = temp
        return str(max_num)
        
result = Solution()
number = "1231"
digit = "1"
ans = result.removeDigit(number,digit)
print(ans)
