class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        pq, chairs = [], []
        taken = {}

        for i, (arrive, leave) in enumerate(times):
            heappush(chairs, i)
            pq.append((arrive, True, i))
            pq.append((leave, False, i))

        pq.sort()

        for time, take, person in pq:
            if take:
                taken[person] = heappop(chairs)
                if person == targetFriend:
                    return taken[person]
            else:
                heappush(chairs, taken[person])
                
            
