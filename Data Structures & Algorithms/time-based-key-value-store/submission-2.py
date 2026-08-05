class TimeMap:

    def __init__(self):
        self._dict = {} # key : list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self._dict:
            self._dict[key] = [] 
        self._dict[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self._dict.get(key, None)
        if not values:
            return res

        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2

            if values[m][1] == timestamp:
                return values[m][0]
            elif values[m][1] < timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return res



