def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
   if not candidates:
       return [] 
   candidates.sort()
   res = []
   def findCombinationSum(nums: list[int], target: int, index: int, curr: list[int]):
       if target <= 0:
           if target == 0:
               res.append(curr[:])
           return
       for i in range(index, len(nums)):
           if nums[i] > target:
               break
           curr.append(nums[i])
           findCombinationSum(nums, target - nums[i], i, curr)
           curr.pop() 
   findCombinationSum(candidates, target, 0, [])
   return res
def test():
   print(combinationSum([2,3,6,7], 7))  
   print(combinationSum([2,3,5], 8))   
   print(combinationSum([2], 1))        
test()
