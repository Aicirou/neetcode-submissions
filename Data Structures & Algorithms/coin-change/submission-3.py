class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        if amount == 0:
            return 0

        seen = [False] * (amount + 1)
        seen[0] = True
        queue = deque([0])
        num = 0
        while queue:
            num += 1
            for _ in range(len(queue)):
                myamt = queue.popleft()

                for coin in coins:
                    newamt = myamt + coin
                    if newamt > amount or seen[newamt]:
                        continue
                    if myamt + coin == amount:
                        return num
                    queue.append(newamt)
                    seen[newamt] = True
        return -1