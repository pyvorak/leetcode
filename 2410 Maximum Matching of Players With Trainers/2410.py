class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i = 0

        for t in trainers:
            if players[i] <= t:
                i += 1
                if i >= len(players):
                    break
        
        return i
