class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left = 0
        right = len(skill) - 1
        sum1 = 0
        x = skill[left] + skill[right]
        while left < right:
            if skill[left] + skill[right] == x:
                sum1 += skill[left] * skill[right]
                right -= 1
                left += 1
            else:
                return -1 
        return sum1 
