'''
Given an integer array "nums", return true if any value appears more than
once in the array, false otherwise

Example 1:
nums = [1, 2, 3, 3]
output = true

Example 2:
nums = [1, 2, 3, 4]
output = false

Initial Analysis:
Problem requires a method of  keeping track of the duplicates within the array.
Therefore, a hashmap is a valid solution.
'''

# My solution:
class Solution:
  def hasDuplicate(self, nums: List[int]) -> bool:
    #initialize an empty dictionary
    counter = {}

    for num in nums:
      if num not in counter:
        counter[num] = 0
      elif num in counter:
        return True

    return False

# Their solution:
class OtherSolution:
  def otherHasDuplicate(self, nums: List[int]) -> bool:
    hashset = set()

    for n in nums:
      if n in hashset:
        return True
    hashset.add(n)

    return False

'''
Time Complexity:
O(n)
'''
