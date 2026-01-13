class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        final = []
        while i < len(word1) and j < len(word2):
            final.append(word1[i])
            final.append(word2[j])
            i += 1
            j += 1

        final.append(word1[i:])
        final.append(word2[j:])

        return "".join(final)


# --- TESTING HARNESS ---
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {
            "name": "Equal Lengths (Example 1)",
            "word1": "abc",
            "word2": "pqr",
            "expected": "apbqcr",
        },
        {
            "name": "Word2 is Longer (Example 2)",
            "word1": "ab",
            "word2": "pqrs",
            "expected": "apbqrs",
        },
        {
            "name": "Word1 is Longer (Example 3)",
            "word1": "abcd",
            "word2": "pq",
            "expected": "apbqcd",
        },
        {"name": "Single Characters", "word1": "a", "word2": "b", "expected": "ab"},
        {
            "name": "One word is significantly longer",
            "word1": "a",
            "word2": "bcdef",
            "expected": "abcdef",
        },
        {
            "name": "Minimum constraints (1 char each)",
            "word1": "x",
            "word2": "y",
            "expected": "xy",
        },
        {
            "name": "Duplicate characters",
            "word1": "aaaa",
            "word2": "bb",
            # Correct logic: a (w1) b (w2) a (w1) b (w2) aa (w1) = ababaa
            "expected": "ababaa",
        },
    ]

    print(f"{'Test Case':<35} | {'Status':<10}")
    print("-" * 50)

    for case in test_cases:
        actual = sol.mergeAlternately(case["word1"], case["word2"])
        status = "✅ PASS" if actual == case["expected"] else f"❌ FAIL (Got: {actual})"
        print(f"{case['name']:<35} | {status}")
