
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Step 1: Find the maximum number of candies any kid currently has
        max_candies = max(candies)
        
        # Step 2: For each kid, check if they can reach or exceed max after getting    extraCandies
        result = [candy + extraCandies >= max_candies for candy in candies]
        
        # Step 3: Return the result list
        return result

# This part runs only when the script is executed directly
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3
    print("Test 1 Output:", sol.kidsWithCandies(candies, extraCandies))  
  

    # Test Case 2
    candies = [4, 2, 1, 1, 2]
    extraCandies = 1
    print("Test 2 Output:", sol.kidsWithCandies(candies, extraCandies))  
    

    # Test Case 3
    candies = [12, 1, 12]
    extraCandies = 10
    print("Test 3 Output:", sol.kidsWithCandies(candies, extraCandies))  
    

        