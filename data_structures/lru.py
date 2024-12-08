class LRUCache:

  def __init__(self, capacity: int):
    self.cache_map = dict()
    self.capacity = capacity

  def get(self, key: int) -> int:
    if key in cache_map:

      return self.cache_map[key]
    else:
      return -1
      
  def put(self, key: int, value: int) -> None:
        pass


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)