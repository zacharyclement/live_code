from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pass


# --- TESTING HARNESS ---
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {
            "name": "Standard Case (Example 1)",
            "prices": [10, 1, 5, 6, 7, 1],
            "expected": 6,  # Buy at 1, sell at 7
        },
        {
            "name": "Decreasing Prices (Example 2)",
            "prices": [10, 8, 7, 5, 2],
            "expected": 0,  # Never profitable
        },
        {
            "name": "Single Day",
            "prices": [5],
            "expected": 0,  # Need at least two days
        },
        {"name": "Flat Prices", "prices": [3, 3, 3, 3], "expected": 0},
        {
            "name": "Price Jumps at End",
            "nums": [1, 2, 10],
            "prices": [7, 1, 5, 3, 6, 4, 15],
            "expected": 14,  # Buy at 1, sell at 15
        },
    ]

    print(f"{'Test Case':<30} | {'Expected':<10} | {'Actual':<10} | {'Status'}")
    print("-" * 70)

    for case in test_cases:
        actual = sol.maxProfit(case["prices"])
        status = "✅ PASS" if actual == case["expected"] else f"❌ FAIL"
        print(
            f"{case['name']:<30} | {str(case['expected']):<10} | {str(actual):<10} | {status}"
        )
