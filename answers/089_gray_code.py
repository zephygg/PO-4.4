# 89. gray code
# i ^ (i >> 1) gives the i-th gray code. O(2^n)
class Solution:
    def grayCode(self, n):
        return [i ^ (i >> 1) for i in range(1 << n)]
