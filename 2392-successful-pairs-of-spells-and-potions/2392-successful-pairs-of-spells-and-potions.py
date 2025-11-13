class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        pairs = []
        potions.sort()
        n, m = len(spells), len(potions)
        for spell in spells:
            if spell >= success:
                pairs.append(m)
                continue
            rem = math.ceil(success / spell)
            idx = bisect.bisect_left(potions, rem)
            pairs.append(m - idx)
        return pairs