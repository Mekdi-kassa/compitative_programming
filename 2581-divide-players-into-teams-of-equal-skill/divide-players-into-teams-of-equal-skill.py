class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        
        skill.sort()
        total = 0
        left = 0 
        right = len(skill) - 1
        target  = skill[left] + skill[right]
        while left < right:
            if skill[left] + skill[right] != target:
                return -1
            total += (skill[left] * skill[right])
            right -= 1
            left += 1
        return total