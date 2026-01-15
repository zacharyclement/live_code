from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # two stesp.
        # step 1, fill all but last entry in nums1

        if n == 0:
            return

        m = m - 1  # last non-zero entry
        n = n - 1  # end of nums 2
        p_write = len(nums1) - 1  # end of nums 1

        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[p_write] = nums1[m]
                m -= 1
            else:
                nums1[p_write] = nums2[n]
                n -= 1
            p_write -= 1

        while n >= 0:
            nums1[p_write] = nums2[n]
            n -= 1
            p_write -= 1

        return nums1


# --- TESTING HARNESS ---
def run_tests():
    sol = Solution()

    test_cases = [
        {
            "name": "Standard Mixed (Example 1)",
            "nums1": [1, 2, 3, 0, 0, 0],
            "m": 3,
            "nums2": [2, 5, 6],
            "n": 3,
            "expected": [1, 2, 2, 3, 5, 6],
        },
        {
            "name": "Empty nums2 (Example 2)",
            "nums1": [1],
            "m": 1,
            "nums2": [],
            "n": 0,
            "expected": [1],
        },
        {
            "name": "Empty nums1 (Example 3)",
            "nums1": [0],
            "m": 0,
            "nums2": [1],
            "n": 1,
            "expected": [1],
        },
        {
            "name": "nums2 elements are all smaller",
            "nums1": [4, 5, 6, 0, 0, 0],
            "m": 3,
            "nums2": [1, 2, 3],
            "n": 3,
            "expected": [1, 2, 3, 4, 5, 6],
        },
        {
            "name": "Duplicate values",
            "nums1": [1, 1, 1, 0, 0, 0],
            "m": 3,
            "nums2": [1, 1, 1],
            "n": 3,
            "expected": [1, 1, 1, 1, 1, 1],
        },
    ]

    print(f"{'Test Case':<30} | {'Status'}")
    print("-" * 45)

    for case in test_cases:
        # We work on a copy of nums1 to ensure the harness isn't
        # reusing data between runs if the logic fails.
        nums1_input = list(case["nums1"])
        nums2_input = list(case["nums2"])

        # Method modifies nums1_input in-place
        sol.merge(nums1_input, case["m"], nums2_input, case["n"])

        status = (
            "✅ PASS"
            if nums1_input == case["expected"]
            else f"❌ FAIL (Got: {nums1_input})"
        )
        print(f"{case['name']:<30} | {status}")


if __name__ == "__main__":
    run_tests()
