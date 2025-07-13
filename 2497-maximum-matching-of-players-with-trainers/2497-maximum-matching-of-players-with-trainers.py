class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        
        trainers.sort()
        players.sort()
        i = 0
        j = 0
        count = 0
        while i < len(players) and j < len(trainers):
    
            if players[i] <= trainers[j]:
                count += 1
            else:
                i -= 1
            i += 1
            j += 1
        return count