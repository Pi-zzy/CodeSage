def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
   dp = [[] for _ in range(target + 1)]
   dp[0] = [[]] 
   for num in candidates:
       for i in range(num, target + 1):
           for combo in dp[i - num]:
               dp[i].append(combo + [num])
   return dp[target]
def test():
   print(combinationSum([2,3,6,7], 7))  
   print(combinationSum([2,3,5], 8))    
   print(combinationSum([2], 1))       
test()
