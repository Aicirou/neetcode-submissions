class TimeMap:

    def __init__(self):
        self.store = {} #key: list of [value, timestamp]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        #self.store.setdefault(key, []).append([value, timestamp])
        if key in self.store:
            self.store[key].append([value, timestamp])
        else:
            self.store[key] = [[value, timestamp]]
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])
        if not values:  # Handle empty list case
            return res

        l, r = 0, len(values) - 1
        while(l<=r):
            m = (l+r) // 2
            print(self.store)
            if values[m][1] == timestamp:
                return values[m][0]
            elif values[m][1] < timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res  