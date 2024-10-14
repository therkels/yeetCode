class Solution:
  def asteroidCollision(self, asteroids: list[int]) -> list[int]:
    sim_arr = []
    for asteroid in asteroids:
      if not sim_arr:
        sim_arr.append(asteroid)
        continue
      asteroid_destroyed = False
      while len(sim_arr) > 0:
        last_asteroid = sim_arr[-1]
        #same direction if their directions cancel out
        if last_asteroid/abs(last_asteroid) > 0 and asteroid/abs(asteroid) < 0:
          if abs(last_asteroid) < abs(asteroid):
            sim_arr.pop(-1)
          elif abs(last_asteroid) == abs(asteroid):
            sim_arr.pop(-1)
            asteroid_destroyed = True
            break
          else:
            asteroid_destroyed = True
            break
        else:
          break
      if not asteroid_destroyed:
        sim_arr.append(asteroid)
    return sim_arr
                    
if __name__ == "__main__":
  s = Solution()
  a = [1,-2,-2,-2]
  print(s.asteroidCollision(a))
