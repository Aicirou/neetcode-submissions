"""
# Stack
Intuition:
Cars that start closer to the target are processed first.
For each car, we compute the time it will take to reach the target.
If a car behind reaches the target no faster than the car in front, it will eventually catch up and join the same fleet.
So we only keep the car’s time if it forms a new fleet; otherwise, it merges with the previous one.
Using a stack helps us easily compare each car’s time with the fleet ahead of it.
"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True, key=lambda x: x[0])

        fleets = []
        for p, s in pairs:
            time = (target - p) / s
            if fleets and fleets[-1] >= time:
                continue
            fleets.append(time)

        return len(fleets)

# class Solution:
#     def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
#         cars = [(p, s) for p, s in zip(position, speed)]
#         cars.sort(reverse=True, key=lambda x: x[0])
        
#         fleets = 0
#         time_to_reach = 0
        
#         for p, s in cars:
#             time = (target - p) / s

#             if time > time_to_reach:
#                 fleets += 1
#                 time_to_reach = time  # Update the time to reach for the new fleet
        
#         return fleets
            
