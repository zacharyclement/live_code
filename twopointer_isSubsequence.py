"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is
formed from the original string by deleting some (can be none) of the
characters without disturbing the relative positions of the remaining
characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"Output: false


"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # start a point (i) on s
        # loop through t with index j
        # if t[j] == s[i], then increment i 1
        # at the end see if i == len(s)

        # assume s is the smaller one
        # if s is empty, it is a substring
        #
        if not s:
            return True

        i = 0

        for j in range(len(t)):
            if t[j] == s[i]:
                i += 1
            if len(s) == i:  # this is need for bases like s = 'b', t = 'abc'
                return True

        return i == len(s)


# --- TESTING HARNESS ---
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {
            "name": "Standard Success (Example 1)",
            "s": "abc",
            "t": "ahbgdc",
            "expected": True,
        },
        {
            "name": "Standard Failure (Example 2)",
            "s": "axc",
            "t": "ahbgdc",
            "expected": False,
        },
        {
            "name": "Empty 's' (Subsequence of everything)",
            "s": "",
            "t": "ahbgdc",
            "expected": True,
        },
        {
            "name": "Empty 't' (Only empty 's' can match)",
            "s": "abc",
            "t": "",
            "expected": False,
        },
        {
            "name": "Same characters, wrong order",
            "s": "acb",
            "t": "ahbgdc",
            "expected": False,
        },
        {"name": "Full string match", "s": "hello", "t": "hello", "expected": True},
        {"name": "S is longer than T", "s": "abcdef", "t": "abc", "expected": False},
    ]

    print(f"{'Test Case':<35} | {'Status':<10}")
    print("-" * 50)

    for case in test_cases:
        actual = sol.isSubsequence(case["s"], case["t"])
        status = "✅ PASS" if actual == case["expected"] else f"❌ FAIL (Got: {actual})"
        print(f"{case['name']:<35} | {status}")
