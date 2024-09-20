def maxArea(height: list[int]) -> int:

  if len(height) == 2:
    return 1*min(height)

  max_area = -1

  l = 0
  r = len(height) - 1
  while l!=r:
    l_height = height[l]
    r_height = height[r]

    max_height = r_height
    if l_height < r_height:
      max_height = l_height
      l += 1
    else:
      r -= 1
    
    max_area = max(max_area, (r-l+1)*max_height)

  return max_area

if __name__ == "__main__":
  height = [1,8,6,2,5,4,8,3,7]
  a = maxArea(height)
  print(a)