from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if (flowerbed[i] == 0 and
                (i == 0 or flowerbed[i - 1] == 0) and
                (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)):
                flowerbed[i] = 1  # Plant a flower
                n -= 1  # One less flower to plant
                if n == 0:
                    return True  # All flowers planted successfully
        return n <= 0  # If still flowers left to plant, return False

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.canPlaceFlowers([1, 0, 0, 0, 1], 1))  # Output: True
    print(sol.canPlaceFlowers([1, 0, 0, 0, 1], 2))  # Output: False

        