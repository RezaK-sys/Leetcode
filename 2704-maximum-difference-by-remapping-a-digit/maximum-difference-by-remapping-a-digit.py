class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str = str(num)
        max_val = num
        min_val = num

        for old_digit in '0123456789':
            for new_digit in '0123456789':
                if old_digit == new_digit:
                    continue

                replaced = num_str.replace(old_digit, new_digit)

                new_val = int(replaced)
                max_val = max(max_val, new_val)
                min_val = min(min_val, new_val)

        return max_val - min_val

if __name__== "__main__":
   sol = Solution()
   print(sol.minMaxDifference(11891))
