class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        dhani = 0
        for row in accounts:
            paisa = sum(row)
            if paisa > dhani:
                dhani = paisa

        return dhani



        