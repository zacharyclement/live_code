class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        s = list(s)
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and s[l] not in vowels:
                l += 1
            while r > l and s[r] not in vowels:
                r -= 1

            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        return "".join(s)


# --- TESTING HARNESS ---
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"name": "Mixed Case (Example 1)", "s": "IceCreAm", "expected": "AceCreIm"},
        {"name": "Lowercase (Example 2)", "s": "leetcode", "expected": "leotcede"},
        {"name": "No Vowels", "s": "rhythm", "expected": "rhythm"},
        {"name": "All Vowels", "s": "aeiou", "expected": "uoiea"},
        {"name": "Single Character", "s": "A", "expected": "A"},
        {"name": "Complex String", "s": "hello world!", "expected": "hollo werld!"},
    ]

    print(f"{'Test Case':<25} | {'Status':<10}")
    print("-" * 40)

    for case in test_cases:
        actual = sol.reverseVowels(case["s"])
        status = (
            "✅ PASS" if actual == case["expected"] else f"❌ FAIL (Got: '{actual}')"
        )
        print(f"{case['name']:<25} | {status}")
