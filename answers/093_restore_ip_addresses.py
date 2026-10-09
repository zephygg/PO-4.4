# 93. restore ip addresses
# backtrack: 4 parts, each 0-255 with no leading zeros
class Solution:
    def restoreIpAddresses(self, s):
        res, parts = [], []

        def dfs(start):
            if len(parts) == 4:
                if start == len(s):
                    res.append(".".join(parts))
                return
            for length in range(1, 4):
                if start + length > len(s):
                    break
                seg = s[start:start + length]
                if (seg[0] == "0" and length > 1) or int(seg) > 255:
                    continue
                parts.append(seg)
                dfs(start + length)
                parts.pop()

        dfs(0)
        return res
