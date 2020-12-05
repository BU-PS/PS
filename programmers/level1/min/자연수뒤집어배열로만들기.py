def solution1(n):
  return [int(i) for i in str(n)][::-1]
  
def solution2(n):
  return list(map(int, str(n)))[::-1]