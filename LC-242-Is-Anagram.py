'''
Given two string 's' and 't', return True if the two strings are anagrams of each other,
otherwise return False

-- Example 1--
Input:
s = "racecar", t = "carrace"

Output:
True

-- Example 2 --
Input:
s = "jar", t = "jam"

Output:
False

Initial Analysis:
Anagrams need to have the same # of total letters and numbers of the same letter. If they have
the same number of letters and are equivalent when sorted, then they are an anagram
'''

# My solution:
'''
class Solution:
  def isAnagram(self, s, t):
    if sorted(s) == sorted(t):
      return True
    return False
'''

# My Solution's Time Complexity:
# O(n * log n)

# Their Solution:
class Solution:
  def isAnagram(self, s, t):
    # if the words don't have the same amount of letters, then we can automatically
    # rule out that they are anagrams
    if len(s) != len(t):
      return False

    s_count, t_count = {}, {}

    for i in range(len(s)):
      # if s_count at the index [s[i]] does not exist, then set the count to 0 with the
      # .get() method, otherwise add 1 to the count

      s_count[s[i]] = 1 + s_count.get(s[i], 0)
      t_count[t[i]] = 1 + t_count.get(t[i], 0)

    # iterate through hashmap, if the key does not exist, set it to 0 to avoid key error,
    # if the count of each letter is not the same, return False, otherwise return True
    for c in s_count:
      if s_count[c] != t_count.get(c, 0):
        return False

    return True

s = "racecar"
t = "carrace"
solution = Solution()
result = solution.isAnagram(s, t)

print(result)

# Their solution's Time Complexity:
# O(n)
