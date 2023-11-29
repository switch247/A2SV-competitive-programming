class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        # num + t = x - t
        # x = num +2t
        # Increase or decrease x by 1, and simultaneously increase or decrease num by 1.
        return num + 2*t
