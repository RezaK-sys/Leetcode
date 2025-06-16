class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if str1 and str2 can be formed by repeating the same pattern
        if str1 + str2 != str2 + str1:
            return""
        # Find the greatest common divisor of the lengths
        gcd_len = math.gcd(len(str1),len(str2))
        return str1[:gcd_len]

if __name__ == "__main__":
    sol = Solution()
    print(sol.gcdOfStrings("ABCABC", "ABC"))    
    print(sol.gcdOfStrings("ABABAB", "ABAB"))     
    print(sol.gcdOfStrings("LEET", "CODE"))       