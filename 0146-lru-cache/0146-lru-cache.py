from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.od = OrderedDict()   # key -> value, order = LRU ... MRU

    def get(self, key: int) -> int:
        if key not in self.od:
            return -1
        self.od.move_to_end(key, last=True)  # mark as MRU
        return self.od[key]

    def put(self, key: int, value: int) -> None:
        if key in self.od:
            self.od[key] = value
            self.od.move_to_end(key, last=True)  # bump to MRU
        else:
            if len(self.od) == self.cap:
                self.od.popitem(last=False)  # evict LRU
            self.od[key] = value
