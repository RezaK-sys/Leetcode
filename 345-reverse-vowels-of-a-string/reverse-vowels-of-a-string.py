class Solution:
    def reverseVowels(self, s: str) -> str:
        # Define vowels, both lowercase and uppercase, for quick lookup
        vowels = set("aeiouAEIOU")
        
        # Convert string to list so we can modify characters
        chars = list(s)
        
        # Set two pointers: one from the start, one from the end
        left, right = 0, len(chars) - 1

        # Loop until the pointers meet
        while left < right:
            # Move the left pointer until we find a vowel
            while left < right and chars[left] not in vowels:
                left += 1

            # Move the right pointer until we find a vowel
            while left < right and chars[right] not in vowels:
                right -= 1

            # Swap the vowels
            chars[left], chars[right] = chars[right], chars[left]

            # Move both pointers inward
            left += 1
            right -= 1

        # Join the list back into a string and return the result
        return ''.join(chars)

# Example usage
if __name__ == "__main__":
    solution = Solution()
    print(solution.reverseVowels("IceCreAm"))   # Output: "AceCreIm"
    print(solution.reverseVowels("leetcode"))   # Output: "leotcede"
