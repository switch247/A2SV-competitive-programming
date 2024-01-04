class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        print(skill)
        left, right = 0 , len(skill) -1
        prev = skill[left] + skill[right]
        chemistry = skill[left] * skill[right]
        left+=1
        right-=1
        while left < right:
            if prev!=(skill[left] + skill[right]): return -1
            chemistry += (skill[left]*skill[right])
            left += 1
            right -= 1

        return chemistry