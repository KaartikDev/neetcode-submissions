class MyHashSet:

    def __init__(self):
        self.arr = [0] * 10001 #max 1mil elements. this is O(1m tho...)

    def add(self, key: int) -> None:
        modKey = key % 10001
        self.arr[modKey] = 1

        

    def remove(self, key: int) -> None:
        modKey = key % 10001
        self.arr[modKey] = 0

    def contains(self, key: int) -> bool:
        modKey = key % 10001
        return self.arr[modKey] == 1
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)